from .models import ConfigItem, Configuration
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm
        
class ConfigItemImportForm(NetBoxModelImportForm):
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'description', 'required')
        
class ConfigItemForm(NetBoxModelForm):
    class Meta:
        model = ConfigItem
        fields = ['name', 'type', 'default_value', 'description']

class ConfigItemFilterForm(NetBoxModelFilterSetForm):
    class Meta:
        model = ConfigItem
        fields = ['name', 'type']
        
class ConfigItemBulkEditForm(NetBoxModelForm):
    class Meta:
        model = ConfigItem
        fields = ['type', 'default_value', 'description']

class ConfigurationForm(NetBoxModelForm):
    class Meta:
        model = Configuration
        fields = ['name', 'included_configurations', 'config_items', 'values', 'not_overridable', 'is_final', 'status', 'description']
        
class ConfigurationImportForm(NetBoxModelImportForm):
    class Meta:
        model = Configuration
        fields = ['name', 'included_configurations', 'config_items', 'values', 'not_overridable', 'is_final', 'status', 'description']
        
class ConfigurationFilterForm(NetBoxModelFilterSetForm):
    class Meta:
        model = Configuration
        fields = ['name', 'status', 'is_final']
        
class ConfigurationBulkEditForm(NetBoxModelForm):
    class Meta:
        model = Configuration
        fields = ['status', 'is_final', 'description']