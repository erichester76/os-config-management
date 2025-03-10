from django import forms
from netbox.forms import NetBoxModelForm
from .models import ConfigItem, ConfigSet, OSConfig
from utilities.forms.fields import JSONField

class ConfigItemForm(NetBoxModelForm):
    """
    Form for creating and editing ConfigItem objects.
    """
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'description', 'required', 'tags')

class ConfigSetForm(NetBoxModelForm):
    """
    Form for creating and editing ConfigSet objects.
    """
    values = JSONField(
        label="Configuration Values",
        help_text="Enter key-value pairs as JSON (e.g., {'timezone': 'UTC'})."
    )

    class Meta:
        model = ConfigSet
        fields = ('name', 'description', 'config_items', 'values', 'tags')

class OSConfigForm(NetBoxModelForm):
    """
    Form for creating and editing OSConfig objects.
    """
    class Meta:
        model = OSConfig
        fields = ('name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'tags')