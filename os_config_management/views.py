from netbox.views import generic
from .models import ConfigItem, ConfigSet, OSConfig
from .tables import ConfigItemTable, ConfigSetTable, OSConfigTable
from .filters import ConfigItemFilterSet, ConfigSetFilterSet, OSConfigFilterSet
from .forms import ConfigItemForm, ConfigSetForm, OSConfigForm, ConfigItemFilterForm, ConfigSetFilterForm, OSConfigFilterForm, ConfigItemImportForm, ConfigSetImportForm, OSConfigImportForm , ConfigItemValueFormSet
from netbox.views import generic
from django.urls import reverse
from django.shortcuts import render
from django import forms

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

    def get_success_url(self):
        if not self.object:
            raise ValueError("self.object is None in get_success_url")
        url = reverse('plugins:os_config_management:configitem_list', kwargs={'pk': self.object.pk})
        if url is None:
            raise ValueError("reverse returned None")
        return url
    

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
    form = ConfigSetForm  
    template_name = 'os_config_management/configset_edit.html'

    def get_extra_context(self, request, instance):
        initial_data = []
        if instance and len(instance.values) > 0 and request.method == 'GET': 
            initial_data = ([{'config_item': ci, 'value': instance.values.get(ci.name, '')} for ci in instance.config_items.all()]) 
            
        formset = ConfigItemValueFormSet(
            request.POST if request.method == 'POST' else None,
            initial=initial_data
        )
        
        if formset is None:
            raise ValueError("Formset instantiation returned None")
        return {'formset': formset}

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = ConfigSetForm(request.POST, instance=obj)  # Pass instance to form
        formset = ConfigItemValueFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Save the ConfigSet form first to ensure obj has an ID
            obj = form.save()  # Creates new or updates existing obj

            # Process formset data
            config_items = set()
            values = {}
            for form_data in formset.cleaned_data:
                if not form_data.get('DELETE', False):  # Skip deleted forms
                    config_item = form_data['config_item']  # This is a ConfigItem instance
                    config_items.add(config_item)
                    values[config_item.name] = form_data['value']

            # Set ManyToMany relationship with ConfigItem instances
            obj.config_items.set(config_items)
            obj.values = values
            obj.save()  # Save any additional changes (e.g., values)

            return self.form_valid(form)
        else:
            context = {
                'form': form,
                'formset': formset,
                'object': obj,
            }
            return render(request, self.template_name, context)
     
    def get_success_url(self):
        url = reverse('plugins:os_config_management:configset_list', kwargs={'pk': self.object.pk})
        return url
    
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
    template_name = 'os_config_management/osconfig_edit.html'

    def get_success_url(self):
        if not self.object:
            raise ValueError("self.object is None in get_success_url")
        url = reverse('plugins:os_config_management:osconfig_list', kwargs={'pk': self.object.pk})
        if url is None:
            raise ValueError("reverse returned None")
        return url
    
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