from netbox.api.serializers import NetBoxModelSerializer
from ..models import ConfigItem, ConfigSet, OSConfig

class ConfigItemSerializer(NetBoxModelSerializer):
    class Meta:
        model = ConfigItem
        fields = "__all__"
        
class ConfigSetSerializer(NetBoxModelSerializer):
    class Meta:
        model = ConfigSet
        fields = "__all__"

class OSConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = OSConfig
        fields = "__all__"
