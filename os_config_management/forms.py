from .models import ConfigItem, Configuration, ConfigItemAssignment
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm
from django.forms import inlineformset_factory
from django import forms

ConfigItemAssignmentFormSet = inlineformset_factory(
    Configuration,
    ConfigItemAssignment,
    fields=('config_item', 'value', 'not_overridable'),
    extra=1,
    can_delete=True,
    can_order=True
)

class ConfigItemImportForm(NetBoxModelImportForm):
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'default_value', 'description' )
        
class ConfigItemForm(NetBoxModelForm):
    default_value = forms.CharField(required=False)
    
    class Meta:
        model = ConfigItem
        fields = ['name', 'type', 'default_value', 'description']

class ConfigItemFilterForm(NetBoxModelFilterSetForm):
    model = ConfigItem

    class Meta:
        model = ConfigItem
        fields = ['name', 'type']
        
class ConfigItemBulkEditForm(NetBoxModelForm):
    default_value = forms.CharField(required=False)

    class Meta:
        model = ConfigItem
        fields = ['type', 'default_value', 'description']

class ConfigurationForm(NetBoxModelForm):
    class Meta:
        model = Configuration
        fields = ['name' 'is_final', 'status', 'description']
        
class ConfigurationImportForm(NetBoxModelImportForm):
    class Meta:
        model = Configuration
        fields = ['name', 'included_configurations', 'config_values', 'is_final', 'status', 'description']
        
class ConfigurationFilterForm(NetBoxModelFilterSetForm):
    model = Configuration

    class Meta:
        model = Configuration
        fields = ['name', 'status', 'is_final']
        
class ConfigurationBulkEditForm(NetBoxModelForm):
    class Meta:
        model = Configuration
        fields = ['status', 'is_final', 'description']