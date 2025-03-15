from netbox.views import generic
from .models import ConfigItem, Configuration
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm, ConfigItemImportForm, ConfigurationImportForm, ConfigItemBulkEditForm, ConfigurationBulkEditForm

# ConfigItem Views
class ConfigItemListView(generic.ObjectListView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    filterset = ConfigItemFilter

class ConfigItemEditView(generic.ObjectEditView):
    queryset = ConfigItem.objects.all()
    model_form = ConfigItemForm

class ConfigItemDetailView(generic.ObjectView):
    queryset = ConfigItem.objects.all()

class ConfigItemChangelogView(generic.ObjectChangelogView):
    queryset = ConfigItem.objects.all()

class ConfigItemBulkEditView(generic.ObjectBulkEditView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    form = ConfigItemBulkEditForm  

class ConfigItemBulkDeleteView(generic.ObjectBulkDeleteView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable

class ConfigItemImportView(generic.ObjectImportView):
    model = ConfigItem
    form = ConfigItemImportForm  

# Configuration Views
class ConfigurationListView(generic.ObjectListView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    filterset = ConfigurationFilter

class ConfigurationEditView(generic.ObjectEditView):
    queryset = Configuration.objects.all()
    model_form = ConfigurationForm

class ConfigurationDetailView(generic.ObjectView):
    queryset = Configuration.objects.all()

    def get_extra_context(self, request, instance):
        config_items_with_origin = []
        inherited_config = instance.inherited_config
        for key, value in inherited_config.items():
            origin = "Default" if key in ConfigItem.objects.values_list('name', flat=True) else "Inherited"
            config_items_with_origin.append({
                'name': key,
                'value': value,
                'origin': origin
            })
        return {'config_items_with_origin': config_items_with_origin}

class ConfigurationChangelogView(generic.ObjectChangelogView):
    queryset = Configuration.objects.all()

class ConfigurationBulkEditView(generic.ObjectBulkEditView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    form = ConfigurationBulkEditForm  

class ConfigurationBulkDeleteView(generic.ObjectBulkDeleteView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable

class ConfigurationImportView(generic.ObjectImportView):
    model = Configuration
    form = ConfigurationImportForm 

