from netbox.views import generic
from .models import ConfigItem, Configuration
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm, ConfigItemFilterForm, ConfigItemImportForm, ConfigurationFilterForm, ConfigurationImportForm, ConfigItemBulkEditForm, ConfigurationBulkEditForm, ConfigItemAssignmentFormSet


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
        assignment_formset = ConfigItemAssignmentFormSet(instance=instance)
        return {'assignment_formset': assignment_formset}

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.get_form()
        assignment_formset = ConfigItemAssignmentFormSet(request.POST, instance=obj)

        if form.is_valid() and assignment_formset.is_valid():
            obj = form.save()
            assignment_formset.save()
            return self.form_valid(form)
        else:
            context = self.get_context_data(form=form, assignment_formset=assignment_formset)
            return render(request, self.template_name, context)
    
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

