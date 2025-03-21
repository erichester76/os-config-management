from .models import ConfigItem, Configuration
from netbox.filtersets import NetBoxModelFilterSet
import django_filters

class ConfigItemFilter(NetBoxModelFilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.ChoiceFilter(choices=ConfigItem._meta.get_field('type').choices)

    class Meta:
        model = ConfigItem
        fields = ['name', 'type']

class ConfigurationFilter(NetBoxModelFilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=Configuration._meta.get_field('status').choices)
    is_final = django_filters.BooleanFilter()

    class Meta:
        model = Configuration
        fields = ['name', 'status', 'is_final']