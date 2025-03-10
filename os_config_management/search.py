from netbox.search import SearchIndex, register_search
from .models import ConfigItem, ConfigSet, OSConfig
import logging

logger = logging.getLogger(__name__)

@register_search
class ConfigItemIndex(SearchIndex):
    """
    Search index for ConfigItem model.
    """
    model = ConfigItem
    fields = (
        ('name', 100),
        ('description', 50),
        ('type', 50),
        ('required', 50),
    )

    def get_queryset(self):
        logger.debug("Indexing ConfigItem objects")
        return ConfigItem.objects.all()

@register_search
class ConfigSetIndex(SearchIndex):
    """
    Search index for ConfigSet model.
    """
    model = ConfigSet
    fields = (
        ('name', 100),
        ('description', 50),
        ('values', 50),
    )

    def get_queryset(self):
        logger.debug("Indexing ConfigSet objects")
        return ConfigSet.objects.all()

@register_search
class OSConfigIndex(SearchIndex):
    """
    Search index for OSConfig model.
    """
    model = OSConfig
    fields = (
        ('name', 100),
        ('description', 50),
        ('hierarchy_type', 50),
        ('state', 50),
    )

    def get_queryset(self):
        logger.debug("Indexing OSConfig objects")
        return OSConfig.objects.all()