from django import forms
from .models import ConfigItem, ConfigSet, OSConfig
from utilities.forms.fields import JSONField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm

class ConfigItemForm(NetBoxModelForm):
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
            
class OSConfigForm(forms.ModelForm):
    class Meta:
        model = OSConfig
        fields = [
            'name', 'description', 'parent', 'hierarchy_type', #'is_machine_specific',
            'state', 'config_sets'
        ]
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'hierarchy_type': forms.Select(attrs={'class': 'form-control'}),
            #'is_machine_specific': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'config_sets': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Exclude the current instance from parent choices to avoid self-referencing
            self.fields['parent'].queryset = OSConfig.objects.exclude(pk=self.instance.pk)
        else:
            self.fields['parent'].queryset = OSConfig.objects.all()
            
class OSConfigFilterForm(NetBoxModelFilterSetForm):
    model = OSConfig
    
class OSConfigImportForm(NetBoxModelImportForm):
    class Meta:
        model = OSConfig
        fields = ('name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'tags')
