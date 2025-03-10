from netbox.api.viewsets import NetBoxModelViewSet
from ..models import ConfigItem, ConfigSet, OSConfig
from .serializers import ConfigItemSerializer, ConfigSetSerializer, OSConfigSerializer

class ConfigItemViewSet(NetBoxModelViewSet):
    queryset = ConfigItem.objects.all()
    serializer_class = ConfigItemSerializer

class ConfigSetViewSet(NetBoxModelViewSet):
    queryset = ConfigSet.objects.all()
    serializer_class = ConfigSetSerializer

class OSConfigViewSet(NetBoxModelViewSet):
    queryset = OSConfig.objects.all()
    serializer_class = OSConfigSerializer