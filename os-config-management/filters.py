from netbox.filtersets import NetBoxModelFilterSet
from .models import ConfigItem, ConfigSet, OSConfig
from django.db.models import Q

class ConfigItemFilterSet(NetBoxModelFilterSet):
    """
    Filter set for ConfigItem objects.
    """
    class Meta:
        model = ConfigItem
        fields = {
            'name': ['exact', 'icontains'],
            'type': ['exact'],
            'required': ['exact'],
        }

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )

class ConfigSetFilterSet(NetBoxModelFilterSet):
    """
    Filter set for ConfigSet objects.
    """
    class Meta:
        model = ConfigSet
        fields = {
            'name': ['exact', 'icontains'],
            'config_items': ['exact'],
        }

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )

class OSConfigFilterSet(NetBoxModelFilterSet):
    """
    Filter set for OSConfig objects.
    """
    class Meta:
        model = OSConfig
        fields = {
            'name': ['exact', 'icontains'],
            'parent': ['exact'],
            'config_sets': ['exact'],
            'hierarchy_type': ['exact'],
            'is_machine_specific': ['exact'],
            'state': ['exact'],
        }

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )