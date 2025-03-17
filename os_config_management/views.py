from netbox.views import generic
from .models import ConfigItem, Configuration
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm, ConfigItemFilterForm, ConfigItemImportForm, ConfigurationFilterForm, ConfigurationImportForm, ConfigItemBulkEditForm, ConfigurationBulkEditForm, ConfigItemAssignmentFormSet, ConfigurationInclusionFormSet
from django.urls import reverse

# ConfigItem Views
class ConfigItemListView(generic.ObjectListView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    filterset = ConfigItemFilter
    filterset_form = ConfigItemFilterForm

class ConfigItemEditView(generic.ObjectEditView):
    queryset = ConfigItem.objects.all()
    form = ConfigItemForm

class ConfigItemDeleteView(generic.ObjectDeleteView):
    queryset = ConfigItem.objects.all()

class ConfigItemDetailView(generic.ObjectView):
    queryset = ConfigItem.objects.all()

class ConfigItemChangelogView(generic.ObjectChangeLogView):
    queryset = ConfigItem.objects.all()

class ConfigItemBulkEditView(generic.BulkEditView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    form = ConfigItemBulkEditForm  

class ConfigItemBulkDeleteView(generic.BulkDeleteView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable

class ConfigItemImportView(generic.BulkImportView):
    queryset = ConfigItem.objects.all()
    model = ConfigItem
    model_form = ConfigItemImportForm  

# Configuration Views
class ConfigurationListView(generic.ObjectListView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    filterset = ConfigurationFilter
    filterset_form = ConfigurationFilterForm
    
class ConfigurationEditView(generic.ObjectEditView):
    queryset = Configuration.objects.all()
    form = ConfigurationForm
    template_name = 'os_config_management/configuration_edit.html'

    def get_extra_context(self, request, instance):
        
        included_formset = ConfigurationInclusionFormSet(
            data=self.request.POST if request.method == "POST" else None, 
            instance=instance
        )
        
        item_formset = ConfigItemAssignmentFormSet(
            data=self.request.POST if request.method == "POST" else None, 
            instance=instance
        )
        
        inherited_items = []
        
        if instance.pk:
            inherited_config = instance.get_inherited_config()  
            for name, value in inherited_config.items():
                try:
                    config_item = ConfigItem.objects.get(name=name)
                    inherited_items.append({
                        'id': config_item.id,
                        'name': name,
                        'value': value
                    })
                except ConfigItem.DoesNotExist:
                    continue
        
        return {
            'included_formset': included_formset,
            'item_formset': item_formset,
            'inherited_items': inherited_items
        }

    def get_success_url(self):
        return reverse('plugins:os_configuration_management:configuration', kwargs={'pk': self.object.pk})
    
class ConfigurationDeleteView(generic.ObjectDeleteView):
    queryset = Configuration.objects.all()

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

class ConfigurationChangelogView(generic.ObjectChangeLogView):
    queryset = Configuration.objects.all()

class ConfigurationBulkEditView(generic.BulkEditView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    form = ConfigurationBulkEditForm  

class ConfigurationBulkDeleteView(generic.BulkDeleteView):
    queryset = Configuration.objects.all()
    table = ConfigurationTable

class ConfigurationImportView(generic.BulkImportView):
    queryset = ConfigItem.objects.all()
    model = Configuration
    model_form = ConfigurationImportForm 

