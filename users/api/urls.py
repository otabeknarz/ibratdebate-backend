from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('regions', views.RegionViewSet)
router.register('districts', views.DistrictViewSet)

auth_router = DefaultRouter()
auth_router.register('token', TokenObtainPairView)
auth_router.register('token-refresh', TokenRefreshView)

urlpatterns = router.urls + auth_router.urls
