from netbox.views import generic
from .models import ConfigItem, Configuration
from .tables import ConfigItemTable, ConfigurationTable
from .filters import ConfigItemFilter, ConfigurationFilter
from .forms import ConfigItemForm, ConfigurationForm, ConfigItemImportForm, ConfigurationImportForm, ConfigItemBulkEditForm, ConfigurationBulkEditForm

# ConfigItem Views
class ConfigItemListView(generic.ObjectListView):
    """View for listing all ConfigItems."""
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    filterset = ConfigItemFilter

class ConfigItemEditView(generic.ObjectEditView):
    """View for adding or editing a ConfigItem."""
    queryset = ConfigItem.objects.all()
    model_form = ConfigItemForm

class ConfigItemDetailView(generic.ObjectView):
    """View for displaying a single ConfigItem's details."""
    queryset = ConfigItem.objects.all()

class ConfigItemChangelogView(generic.ObjectChangelogView):
    """View for displaying the changelog of a ConfigItem."""
    queryset = ConfigItem.objects.all()

class ConfigItemBulkEditView(generic.ObjectBulkEditView):
    """View for bulk editing ConfigItems."""
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable
    form = ConfigItemBulkEditForm  # Assumes this form is defined in forms.py

class ConfigItemBulkDeleteView(generic.ObjectBulkDeleteView):
    """View for bulk deleting ConfigItems."""
    queryset = ConfigItem.objects.all()
    table = ConfigItemTable

class ConfigItemImportView(generic.ObjectImportView):
    """View for importing ConfigItems."""
    model = ConfigItem
    form = ConfigItemImportForm  # Assumes this form is defined in forms.py

# Configuration Views
class ConfigurationListView(generic.ObjectListView):
    """View for listing all Configurations."""
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    filterset = ConfigurationFilter

class ConfigurationEditView(generic.ObjectEditView):
    """View for adding or editing a Configuration."""
    queryset = Configuration.objects.all()
    model_form = ConfigurationForm

class ConfigurationDetailView(generic.ObjectView):
    """View for displaying a single Configuration's details."""
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

class ConfigurationChangelogView(generic.ObjectChangelogView):
    """View for displaying the changelog of a Configuration."""
    queryset = Configuration.objects.all()

class ConfigurationBulkEditView(generic.ObjectBulkEditView):
    """View for bulk editing Configurations."""
    queryset = Configuration.objects.all()
    table = ConfigurationTable
    form = ConfigurationBulkEditForm  # Assumes this form is defined in forms.py

class ConfigurationBulkDeleteView(generic.ObjectBulkDeleteView):
    """View for bulk deleting Configurations."""
    queryset = Configuration.objects.all()
    table = ConfigurationTable

class ConfigurationImportView(generic.ObjectImportView):
    """View for importing Configurations."""
    model = Configuration
    form = ConfigurationImportForm  # Assumes this form is defined in forms.py

