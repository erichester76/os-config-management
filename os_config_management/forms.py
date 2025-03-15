from django import forms
from .models import ConfigItem, Configuration

class ConfigItemForm(forms.ModelForm):
    class Meta:
        model = ConfigItem
        fields = ['name', 'type', 'default_value', 'description']

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ['name', 'included_configurations', 'config_items', 'values', 'not_overridable', 'is_final', 'status', 'description']