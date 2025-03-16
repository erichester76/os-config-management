from netbox.views import generic
from .models import ConfigItem, Configuration, ConfigurationInclusion
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm, ConfigItemFilterForm, ConfigItemImportForm, ConfigurationFilterForm, ConfigurationImportForm, ConfigItemBulkEditForm, ConfigurationBulkEditForm, ConfigItemAssignmentFormSet, ConfigurationInclusionFormSet


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
    model = Configuration
    form_class = ConfigurationForm
    template_name = 'configuration_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['linked_formset'] = ConfigurationInclusionFormSet(self.request.POST, instance=self.object)
            context['item_formset'] = ConfigItemAssignmentFormSet(self.request.POST, instance=self.object)
        else:
            context['linked_formset'] = ConfigurationInclusionFormSet(instance=self.object)
            context['item_formset'] = ConfigItemAssignmentFormSet(instance=self.object)
        
        # Compute inherited items (assuming a method exists or needs to be implemented)
        inherited_config = self.object.get_inherited_config()  # Returns {name: value}
        inherited_items = []
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
        context['inherited_items'] = inherited_items
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        linked_formset = context['linked_formset']
        item_formset = context['item_formset']
        if linked_formset.is_valid() and item_formset.is_valid():
            self.object = form.save()
            linked_formset.instance = self.object
            linked_formset.save()
            item_formset.instance = self.object
            item_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
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

