from netbox.views import generic
from .models import ConfigItem, ConfigSet, OSConfig
from .tables import ConfigItemTable, ConfigSetTable, OSConfigTable
from .filters import ConfigItemFilterSet, ConfigSetFilterSet, OSConfigFilterSet
from .forms import ConfigItemForm, ConfigSetForm, OSConfigForm, ConfigItemFilterForm, ConfigSetFilterForm, OSConfigFilterForm, ConfigItemImportForm, ConfigSetImportForm, OSConfigImportForm    
from utilities.forms import CSVModelForm
import csv
from io import StringIO
from django.http import HttpResponse
from django import forms

# ConfigItem Views
class ConfigItemListView(generic.ObjectListView):
    queryset = ConfigItem.objects.all()
    table_class = ConfigItemTable
    filterset = ConfigItemFilterSet
    filterset_form = ConfigItemFilterForm

class ConfigItemView(generic.ObjectView):
    queryset = ConfigItem.objects.all()

class ConfigItemEditView(generic.ObjectEditView):
    queryset = ConfigItem.objects.all()
    form_class = ConfigItemForm

class ConfigItemDeleteView(generic.ObjectDeleteView):
    queryset = ConfigItem.objects.all()

class ConfigItemBulkEditView(generic.BulkEditView):
    queryset = ConfigItem.objects.all()
    filterset = ConfigItemFilterSet
    table_class = ConfigItemTable
    form_class = ConfigItemForm

class ConfigItemBulkDeleteView(generic.BulkDeleteView):
    queryset = ConfigItem.objects.all()
    filterset = ConfigItemFilterSet
    table_class = ConfigItemTable

class ConfigItemImportView(generic.ObjectImportView):
    queryset = ConfigItem.objects.all()
    model_form = ConfigItemImportForm
    model = ConfigItem
    
class ConfigItemChangeLogView(generic.ObjectChangeLogView):
    queryset = ConfigItem.objects.all()
    
# ConfigSet Views
class ConfigSetListView(generic.ObjectListView):
    queryset = ConfigSet.objects.all()
    table_class = ConfigSetTable
    filterset = ConfigSetFilterSet
    filterset_form = ConfigSetFilterForm

class ConfigSetView(generic.ObjectView):
    queryset = ConfigSet.objects.all()

class ConfigSetEditView(generic.ObjectEditView):
    queryset = ConfigSet.objects.all()
    form_class = ConfigSetForm

class ConfigSetDeleteView(generic.ObjectDeleteView):
    queryset = ConfigSet.objects.all()

class ConfigSetBulkEditView(generic.BulkEditView):
    queryset = ConfigSet.objects.all()
    filterset = ConfigSetFilterSet
    table_class = ConfigSetTable
    form_class = ConfigSetForm

class ConfigSetBulkDeleteView(generic.BulkDeleteView):
    queryset = ConfigSet.objects.all()
    filterset = ConfigSetFilterSet
    table_class = ConfigSetTable

class ConfigSetImportView(generic.ObjectImportView):
    queryset = ConfigSet.objects.all()
    model_form = ConfigSetImportForm
    model = ConfigSet
    
class ConfigSetChangeLogView(generic.ObjectChangeLogView):
    queryset = ConfigSet.objects.all()
    
# OSConfig Views
class OSConfigListView(generic.ObjectListView):
    queryset = OSConfig.objects.all()
    table_class = OSConfigTable
    filterset = OSConfigFilterSet
    filterset_form = OSConfigFilterForm

class OSConfigView(generic.ObjectView):
    queryset = OSConfig.objects.all()

class OSConfigEditView(generic.ObjectEditView):
    queryset = OSConfig.objects.all()
    form_class = OSConfigForm

class OSConfigDeleteView(generic.ObjectDeleteView):
    queryset = OSConfig.objects.all()

class OSConfigBulkEditView(generic.BulkEditView):
    queryset = OSConfig.objects.all()
    filterset = OSConfigFilterSet
    table_class = OSConfigTable
    form_class = OSConfigForm

class OSConfigBulkDeleteView(generic.BulkDeleteView):
    queryset = OSConfig.objects.all()
    filterset = OSConfigFilterSet
    table_class = OSConfigTable

class OSConfigImportView(generic.ObjectImportView):
    queryset = OSConfig.objects.all()
    model_form = OSConfigImportForm
    model = OSConfig

class OSConfigChangeLogView(generic.ObjectChangeLogView):
    queryset = OSConfig.objects.all()