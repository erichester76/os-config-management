from django.db import models
from netbox.models import NetBoxModel
from django.core.exceptions import ValidationError
import logging
from django.urls import reverse

logger = logging.getLogger(__name__)

class ConfigItem(NetBoxModel):
    """
    Defines a configuration key with its type and metadata, used in ConfigSet.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique name of the configuration key (e.g., 'timezone', 'dns_servers')."
    )
    type = models.CharField(
        max_length=50,
        choices=[('string', 'String'), ('list', 'List'), ('boolean', 'Boolean')],
        default='string',
        help_text="Type of the configuration value (e.g., 'string', 'list')."
    )
    description = models.TextField(
        blank=True,
        help_text="Description of the configuration key."
    )
    required = models.BooleanField(
        default=False,
        help_text="Whether a value is required for this key."
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Config Item"
        verbose_name_plural = "Config Items"

    def __str__(self):
        return self.name

    def clean(self):
        if not self.name or not self.name.strip():
            raise ValidationError("Name cannot be empty.")
        super().clean()
        
    def get_absolute_url(self):
        return reverse('plugins:os_config_management:configitem', kwargs={'pk': self.pk})


class ConfigSet(NetBoxModel):
    """
    Groups ConfigItems with specific values, representing a configuration profile.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique name of the configuration set (e.g., 'Linux Global Config')."
    )
    description = models.TextField(
        blank=True,
        help_text="Description of the configuration set."
    )
    config_items = models.ManyToManyField(
        ConfigItem,
        related_name='config_sets',
        help_text="Configuration items allowed in this set."
    )
    values = models.JSONField(
        default=dict,
        blank=True,
        help_text="JSON object of key-value pairs for this configuration set (e.g., {'timezone': 'UTC'})."
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Config Set"
        verbose_name_plural = "Config Sets"

    def __str__(self):
        return self.name

    def clean(self):
        if self.values:
            for key, value in self.values.items():
                if key not in [item.name for item in self.config_items.all()]:
                    raise ValidationError(f"Key '{key}' not defined in ConfigItems for this set.")
                item = next((item for item in self.config_items.all() if item.name == key), None)
                if item.required and not value:
                    raise ValidationError(f"Required key '{key}' cannot have an empty value.")
                if item.type == 'list' and not isinstance(value, (list, str)):
                    raise ValidationError(f"Key '{key}' must be a list or string.")
                elif item.type == 'boolean' and not isinstance(value, bool):
                    raise ValidationError(f"Key '{key}' must be a boolean.")
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('plugins:os_config_management:configset', kwargs={'pk': self.pk})


class OSConfig(NetBoxModel):
    """
    A self-referencing model to manage OS-level configuration hierarchies using multiple ConfigSets.
    Supports multiple hierarchies identified by hierarchy_type, with a method to merge configurations.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="A unique name for this configuration node (e.g., 'Finance', 'Linux', 'East')."
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        help_text="The parent configuration node from which this node inherits Config Sets."
    )
    config_sets = models.ManyToManyField(
        ConfigSet,
        related_name='os_configs',
        blank=True,
        help_text="Configuration sets applied to this node, overriding inherited Config Sets."
    )
    hierarchy_type = models.CharField(
        max_length=50,
        choices=[
            ('regional', 'Regional'),
            ('sizing', 'Sizing'),
            ('os', 'OS'),
            ('network', 'Network'),
        ],
        default='os',
        help_text="The type of hierarchy this node belongs to (e.g., 'regional', 'sizing')."
    )
    is_machine_specific = models.BooleanField(
        default=False,
        help_text="Indicates if this node represents a specific machine (leaf node)."
    )
    description = models.TextField(
        blank=True,
        help_text="Optional description or notes about this configuration."
    )
    state = models.CharField(
        max_length=50,
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        default='active',
        help_text="The status of this configuration."
    )

    class Meta:
        ordering = ['name']
        verbose_name = "OS Configuration"
        verbose_name_plural = "OS Configurations"

    def __str__(self):
        return f"{self.name} (Parent: {self.parent.name if self.parent else 'None'}, Type: {self.hierarchy_type})"

    def get_inherited_config(self):
        """
        Recursively get the inherited configuration for this node within its hierarchy.
        ConfigSets from the current node override those from parent nodes for overlapping keys.
        """
        config = {}
        if self.parent:
            config.update(self.parent.get_inherited_config())
        for config_set in self.config_sets.all():
            config.update(config_set.values)
        return config

    def get_all_config_sets(self):
        """
        Recursively get all ConfigSets from this node and its parents, in order of precedence.
        Returns a list of ConfigSet objects, with the current node's ConfigSets last (highest precedence).
        """
        config_sets = []
        if self.parent:
            config_sets.extend(self.parent.get_all_config_sets())
        config_sets.extend(self.config_sets.all())
        return config_sets

    @staticmethod
    def merge_configs(bottom_nodes):
        """
        Merge configurations from multiple bottom-level nodes of different hierarchies.
        Args:
            bottom_nodes: List of OSConfig objects representing bottom-level nodes from different hierarchies.
        Returns:
            dict: Merged configuration with overrides applied based on hierarchy type precedence.
        """
        merged_config = {}
        # Define precedence order (highest to lowest)
        hierarchy_precedence = ['machine_specific', 'type', 'deployment_type', 'cluster', 'landing_zone', 'region', 'global', 'os', 'organization']
        
        # Group ConfigSets by hierarchy type
        config_sets_by_type = {}
        for node in bottom_nodes:
            if node.is_machine_specific:
                config_sets_by_type['machine_specific'] = node.get_all_config_sets()
            elif node.hierarchy_type:
                config_sets_by_type[node.hierarchy_type] = node.get_all_config_sets()

        # Apply ConfigSets in order of precedence
        for hierarchy in hierarchy_precedence:
            if hierarchy in config_sets_by_type:
                for config_set in config_sets_by_type[hierarchy]:
                    merged_config.update(config_set.values)

        return merged_config
    
    def get_absolute_url(self):
        return reverse('plugins:os_config_management:osconfig', kwargs={'pk': self.pk})
