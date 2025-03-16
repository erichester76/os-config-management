from django.db import models
from netbox.models import NetBoxModel
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from django.urls import reverse

class ConfigItem(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=[('string', 'String'), ('list', 'List'), ('boolean', 'Boolean')])
    default_value = models.JSONField(default=None, null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        """Validate that the default_value matches the specified type."""
        if self.default_value is not None:
            if self.type == 'string' and not isinstance(self.default_value, str):
                raise ValidationError("Default value must be a string.")
            elif self.type == 'list' and not isinstance(self.default_value, list):
                raise ValidationError("Default value must be a list.")
            elif self.type == 'boolean' and not isinstance(self.default_value, bool):
                raise ValidationError("Default value must be a boolean.")
            
    def get_absolute_url(self):
        return reverse('plugins:os_config_management:configitem', args=[self.pk])

class ConfigurationInclusion(models.Model):
    parent_configuration = models.ForeignKey('Configuration', on_delete=models.CASCADE, related_name='inclusions')
    included_configuration = models.ForeignKey('Configuration', on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def clean(self):
        """Check for circular inclusions in the configuration hierarchy."""
        def check_circular(config, visited=None):
            if visited is None:
                visited = set()
            if config.id in visited:
                raise ValidationError("Circular inclusion detected.")
            visited.add(config.id)
            for inclusion in config.inclusions.all():
                check_circular(inclusion.included_configuration, visited.copy())
        check_circular(self.parent_configuration)

class Configuration(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    included_configurations = models.ManyToManyField('self', through='ConfigurationInclusion', symmetrical=False, blank=True)
    config_items = models.ManyToManyField(ConfigItem, blank=True)
    values = models.JSONField(default=dict, blank=True)
    not_overridable = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        """Validate that values match associated config_items and their types."""
        config_item_names = set(self.config_items.values_list('name', flat=True))
        for key in self.values.keys():
            if key not in config_item_names:
                raise ValidationError(f"Key '{key}' in values is not in associated config_items.")
            config_item = ConfigItem.objects.get(name=key)
            value = self.values[key]
            if config_item.type == 'string' and not isinstance(value, str):
                raise ValidationError(f"Value for '{key}' must be a string.")
            elif config_item.type == 'list' and not isinstance(value, list):
                raise ValidationError(f"Value for '{key}' must be a list.")
            elif config_item.type == 'boolean' and not isinstance(value, bool):
                raise ValidationError(f"Value for '{key}' must be a boolean.")
            
    def get_absolute_url(self):
        return reverse('plugins:os_config_management:configuration', args=[self.pk])
    
    @cached_property
    def inherited_config(self):
        """Compute the inherited configuration with caching."""
        config = {}
        # Start with default values from ConfigItems
        for config_item in ConfigItem.objects.all():
            if config_item.default_value is not None:
                config[config_item.name] = config_item.default_value
        # Apply included configurations in order
        inclusions = self.inclusions.all().order_by('order')
        for inclusion in inclusions:
            included_config = inclusion.included_configuration.inherited_config
            if inclusion.included_configuration.not_overridable:
                config.update({k: v for k, v in included_config.items() if k not in config})
            else:
                config.update(included_config)
        # Apply this configuration's values
        if self.not_overridable:
            config.update({k: v for k, v in self.values.items() if k not in config})
        else:
            config.update(self.values)
        return config