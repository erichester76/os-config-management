import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import ConfigItem, ConfigSet, OSConfig

class ConfigItemTable(NetBoxTable):
    """
    Table for displaying ConfigItem objects.
    """
    name = tables.Column(linkify=True)
    type = tables.Column()
    description = tables.Column()
    required = tables.BooleanColumn()

    class Meta(NetBoxTable.Meta):
        model = ConfigItem
        fields = ('pk', 'id', 'name', 'type', 'description', 'required', 'created', 'last_updated')
        default_columns = ('name', 'type', 'description', 'required')

class ConfigSetTable(NetBoxTable):
    """
    Table for displaying ConfigSet objects.
    """
    name = tables.Column(linkify=True)
    description = tables.Column()
    config_items = tables.ManyToManyColumn()
    values = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = ConfigSet
        fields = ('pk', 'id', 'name', 'description', 'config_items', 'values', 'created', 'last_updated')
        default_columns = ('name', 'description', 'values', 'last_updated')

class OSConfigTable(NetBoxTable):
    """
    Table for displaying OSConfig objects.
    """
    name = tables.Column(linkify=True)
    parent = tables.Column(linkify=True)
    config_sets = tables.ManyToManyColumn()
    hierarchy_type = tables.Column()
    is_machine_specific = tables.BooleanColumn()
    description = tables.Column()
    state = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = OSConfig
        fields = ('pk', 'id', 'name', 'parent', 'config_sets', 'hierarchy_type', 'is_machine_specific', 'description', 'state', 'created', 'last_updated')
        default_columns = ('name', 'parent', 'config_sets', 'hierarchy_type', 'last_updated')