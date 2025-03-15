from netbox.search import SearchIndex, register_search
from .models import ConfigItem, Configuration

@register_search
class ConfigItemIndex(SearchIndex):
    model = ConfigItem
    fields = (
        ('name', 100),
        ('description', 500),
    )

@register_search
class ConfigurationIndex(SearchIndex):
    model = Configuration
    fields = (
        ('name', 100),
        ('description', 500),
    )