from netbox.views import generic
from .models import ConfigItem, ConfigSet, OSConfig
from .tables import ConfigItemTable, ConfigSetTable, OSConfigTable
from .filters import ConfigItemFilterSet, ConfigSetFilterSet, OSConfigFilterSet
from .forms import ConfigItemForm, ConfigSetForm, OSConfigForm, ConfigItemFilterForm, ConfigSetFilterForm, OSConfigFilterForm, ConfigItemImportForm, ConfigSetImportForm, OSConfigImportForm , ConfigItemValueFormSet
from netbox.views import generic
from django.urls import reverse_lazy


# ConfigItem Views
class ConfigItemListView(generic.ObjectListView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    filterset = ConfigItemFilterSet
    filterset_form = ConfigItemFilterForm

class ConfigItemView(generic.ObjectView):
    queryset = ConfigItem.objects.all()

class ConfigItemEditView(generic.ObjectEditView):
    queryset = ConfigItem.objects.all()
    form = ConfigItemForm

class ConfigItemDeleteView(generic.ObjectDeleteView):
    queryset = ConfigItem.objects.all()

class ConfigItemBulkEditView(generic.BulkEditView):
    queryset = ConfigItem.objects.all()
    filterset = ConfigItemFilterSet
    table = ConfigItemTable
    form = ConfigItemForm

class ConfigItemBulkDeleteView(generic.BulkDeleteView):
    queryset = ConfigItem.objects.all()
    filterset = ConfigItemFilterSet
    table = ConfigItemTable

class ConfigItemImportView(generic.BulkImportView):
    queryset = ConfigItem.objects.all()
    model_form = ConfigItemImportForm
    model = ConfigItem
    
class ConfigItemChangeLogView(generic.ObjectChangeLogView):
    queryset = ConfigItem.objects.all()
    
# ConfigSet Views
class ConfigSetListView(generic.ObjectListView):
    queryset = ConfigSet.objects.all()
    table = ConfigSetTable
    filterset = ConfigSetFilterSet
    filterset_form = ConfigSetFilterForm

class ConfigSetView(generic.ObjectView):
    queryset = ConfigSet.objects.all()

class ConfigSetEditView(generic.ObjectEditView):
    queryset = ConfigSet.objects.all()
    form_class = ConfigSetForm
    template_name = 'os_config_management/configset_edit.html'

    def get_object(self, **kwargs):
        # Return existing object if pk is provided, otherwise None for creation
        if 'pk' in self.kwargs:
            return super().get_object(**kwargs)
        return None

    def get_form(self, form_class=None):
        # Ensure form works with instance=None for creation
        if form_class is None:
            form_class = self.form_class
        return form_class(self.request.POST if self.request.method == 'POST' else None, instance=self.get_object())

    def get_extra_context(self, request, instance):
        # Prepare formset initial data, empty if instance is None
        initial_data = (
            [{'config_item': ci, 'value': instance.values.get(ci.name, '')}
             for ci in instance.config_items.all()]
            if instance else []
        )
        formset = ConfigItemValueFormSet(
            request.POST if request.method == 'POST' else None,
            initial=initial_data
        )
        return {'formset': formset}

    def post(self, request, *args, **kwargs):
        obj = self.get_object()  # Could be None for creation
        form = self.get_form()
        formset = ConfigItemValueFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Save the instance (creates new if obj was None)
            obj = form.save()

            # Process formset data
            config_items = set()
            values = {}
            for form_data in formset.cleaned_data:
                if not form_data.get('DELETE', False):
                    config_item = form_data['config_item']
                    config_items.add(config_item)
                    values[config_item.name] = form_data['value']

            # Update ManyToManyField and JSONField
            obj.config_items.set(config_items)
            obj.values = values
            obj.save()
            return self.form_valid(form)  # Sets self.object and redirects
        return self.form_invalid(form)

    def get_success_url(self):
        # Use self.object (set by form_valid) instead of get_object()
        return reverse_lazy('plugins:os_config_management:configset', kwargs={'pk': self.object.pk})
    
class ConfigSetDeleteView(generic.ObjectDeleteView):
    queryset = ConfigSet.objects.all()

class ConfigSetBulkEditView(generic.BulkEditView):
    queryset = ConfigSet.objects.all()
    filterset = ConfigSetFilterSet
    table = ConfigSetTable
    form_class = ConfigSetForm

class ConfigSetBulkDeleteView(generic.BulkDeleteView):
    queryset = ConfigSet.objects.all()
    filterset = ConfigSetFilterSet
    table_class = ConfigSetTable

class ConfigSetImportView(generic.BulkImportView):
    queryset = ConfigSet.objects.all()
    model_form = ConfigSetImportForm
    model = ConfigSet
    
class ConfigSetChangeLogView(generic.ObjectChangeLogView):
    queryset = ConfigSet.objects.all()
    
# OSConfig Views
class OSConfigListView(generic.ObjectListView):
    queryset = OSConfig.objects.all()
    table = OSConfigTable
    filterset = OSConfigFilterSet
    filterset_form = OSConfigFilterForm

class OSConfigView(generic.ObjectView):
    queryset = OSConfig.objects.all()

class OSConfigEditView(generic.ObjectEditView):
    queryset = OSConfig.objects.all()
    form = OSConfigForm

class OSConfigDeleteView(generic.ObjectDeleteView):
    queryset = OSConfig.objects.all()

class OSConfigBulkEditView(generic.BulkEditView):
    queryset = OSConfig.objects.all()
    filterset = OSConfigFilterSet
    table = OSConfigTable
    form_class = OSConfigForm

class OSConfigBulkDeleteView(generic.BulkDeleteView):
    queryset = OSConfig.objects.all()
    filterset = OSConfigFilterSet
    table = OSConfigTable

class OSConfigImportView(generic.BulkImportView):
    queryset = OSConfig.objects.all()
    model_form = OSConfigImportForm
    model = OSConfig

class OSConfigChangeLogView(generic.ObjectChangeLogView):
    queryset = OSConfig.objects.all()