from rest_framework import routers
from .views import ConfigItemViewSet, ConfigSetViewSet, OSConfigViewSet

router = routers.DefaultRouter()
router.register('config-items', ConfigItemViewSet)
router.register('config-sets', ConfigSetViewSet)
router.register('os-configs', OSConfigViewSet)

urlpatterns = router.urls