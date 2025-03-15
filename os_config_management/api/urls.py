from rest_framework import routers
from .views import ConfigItemViewSet, ConfigurationViewSet

router = routers.DefaultRouter()
router.register('config-items', ConfigItemViewSet)
router.register('configurations', ConfigurationViewSet)

urlpatterns = router.urls