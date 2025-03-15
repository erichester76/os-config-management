from netbox.views import generic
from .models import ConfigItem, Configuration
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm

class ConfigItemListView(generic.ObjectListView):
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    filterset = ConfigItemFilter

class ConfigItemEditView(generic.ObjectEditView):
    queryset = ConfigItem.objects.all()
    model_form = ConfigItemForm

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
        """Provide inherited config items with their origins for the template."""
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