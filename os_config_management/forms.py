from django import forms
from .models import ConfigItem, ConfigSet, OSConfig
from utilities.forms.fields import JSONField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm

class ConfigItemForm(NetBoxModelForm):
    """
    Form for creating and editing ConfigItem objects.
    """
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'description', 'required', 'tags')

class ConfigItemFilterForm(NetBoxModelFilterSetForm):
    model = ConfigItem
        
class ConfigItemImportForm(NetBoxModelImportForm):
    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'description', 'required')
        

class ConfigSetForm(forms.ModelForm):
    class Meta:
        model = ConfigSet
        fields = ['name', 'description']

class ConfigItemValueForm(forms.Form):
    config_item = forms.ModelChoiceField(
        queryset=ConfigItem.objects.all(),
        label="Config Item",
        widget=forms.Select(attrs={'class': 'form-control config-item-select'})
    )
    value = forms.CharField(
        label="Value",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control config-value'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'config_item' in kwargs['initial']:
            config_item = kwargs['initial']['config_item']
            if config_item.type == 'boolean':
                self.fields['value'] = forms.BooleanField(
                    label="Value",
                    required=False,
                    widget=forms.CheckboxInput(attrs={'class': 'form-check-input config-value'})
                )
            elif config_item.type == 'list':
                self.fields['value'] = forms.CharField(
                    label="Value (comma-separated)",
                    required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control config-value'})
                )

    def clean(self):
        cleaned_data = super().clean()
        config_item = cleaned_data.get('config_item')
        value = cleaned_data.get('value')

        if config_item:
            if config_item.required and not value:
                raise forms.ValidationError(f"'{config_item.name}' is required.")
            if config_item.type == 'boolean':
                cleaned_data['value'] = bool(value)
            elif config_item.type == 'list' and value:
                cleaned_data['value'] = [v.strip() for v in value.split(',') if v.strip()]
        return cleaned_data

# Create the formset
ConfigItemValueFormSet = forms.formset_factory(
    ConfigItemValueForm,
    extra=1,  # Start with 1 empty row
    can_delete=True
)

class ConfigSetFilterForm(NetBoxModelFilterSetForm):
    model = ConfigSet

class ConfigSetImportForm(NetBoxModelImportForm):
    class Meta:
        model = ConfigSet
        fields = ('name', 'description', 'config_items', 'values', 'tags')
            
class OSConfigForm(NetBoxModelForm):
    """
    Form for creating and editing OSConfig objects.
    """
    class Meta:
        model = OSConfig
        fields = ('name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'tags')
        
class OSConfigFilterForm(NetBoxModelFilterSetForm):
    model = OSConfig
    
class OSConfigImportForm(NetBoxModelImportForm):
    class Meta:
        model = OSConfig
        fields = ('name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'tags')
