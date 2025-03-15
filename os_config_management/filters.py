import django_filters
from .models import ConfigItem, Configuration

class ConfigItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.ChoiceFilter(choices=ConfigItem._meta.get_field('type').choices)

    class Meta:
        model = ConfigItem
        fields = ['name', 'type']

class ConfigurationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=Configuration._meta.get_field('status').choices)
    is_final = django_filters.BooleanFilter()

    class Meta:
        model = Configuration
        fields = ['name', 'status', 'is_final']