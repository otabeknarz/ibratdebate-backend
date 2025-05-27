from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('regions', views.RegionViewSet)
router.register('districts', views.DistrictViewSet)

urlpatterns = router.urls
