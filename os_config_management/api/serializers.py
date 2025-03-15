from netbox.api.serializers import NetBoxModelSerializer
from ..models import ConfigItem, Configuration

class ConfigItemSerializer(NetBoxModelSerializer):
    class Meta:
        model = ConfigItem
        fields = '__all__'

class ConfigurationSerializer(NetBoxModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'
