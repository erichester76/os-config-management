from netbox.api.viewsets import NetBoxModelViewSet
from ..models import ConfigItem, Configuration
from .serializers import ConfigItemSerializer, ConfigurationSerializer

class ConfigItemViewSet(NetBoxModelViewSet):
    queryset = ConfigItem.objects.all()
    serializer_class = ConfigItemSerializer

class ConfigurationViewSet(NetBoxModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer