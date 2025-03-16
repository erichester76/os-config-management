from .models import ConfigItem, Configuration
from netbox.tables import NetBoxTable
from django_tables2 import tables

class ConfigItemTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'default_value', 'description')

class ConfigurationTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta:
        model = Configuration
        fields = ('name', 'status', 'is_final', 'description')