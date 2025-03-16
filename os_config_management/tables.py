from .models import ConfigItem, Configuration
from netbox.tables import NetBoxTable
from django_tables2 import tables

class ConfigItemTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ConfigItem
        fields = ('pk', 'id', 'name', 'type', 'default_value', 'description')
        default_columns = ('name', 'description', 'type', 'default_value')

class ConfigurationTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Configuration
        fields = ('pk', 'id', 'name', 'status', 'is_final', 'description')
        default_columns = ('name', 'description', 'status', 'is_final')