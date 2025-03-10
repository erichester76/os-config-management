from django import forms
from .models import ConfigItem, ConfigSet, OSConfig
from utilities.forms.fields import JSONField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm

class ConfigItemForm(NetBoxModelForm):
    """
    Form for creating and editing ConfigItem objects.
    """
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'description', 'required', 'tags')

class ConfigItemFilterForm(NetBoxModelFilterSetForm):
    model = ConfigItem
        
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

class ConfigSetFilterForm(NetBoxModelFilterSetForm):
    model = ConfigSet

            
class OSConfigForm(NetBoxModelForm):
    """
    Form for creating and editing OSConfig objects.
    """
    class Meta:
        model = OSConfig
        fields = ('name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'tags')
        
class OSConfigFilterForm(NetBoxModelFilterSetForm):
    model = OSConfig
