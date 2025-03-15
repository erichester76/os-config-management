import django_tables2 as tables
from .models import ConfigItem, Configuration

class ConfigItemTable(tables.Table):
    name = tables.Column(linkify=True)
    type = tables.Column()
    default_value = tables.Column()

    class Meta:
        model = ConfigItem
        fields = ('name', 'type', 'default_value', 'description')

class ConfigurationTable(tables.Table):
    name = tables.Column(linkify=True)
    status = tables.Column()
    is_final = tables.Column()

    class Meta:
        model = Configuration
        fields = ('name', 'status', 'is_final', 'description')