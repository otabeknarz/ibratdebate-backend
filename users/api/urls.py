from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('regions', views.RegionViewSet)
router.register('districts', views.DistrictViewSet)

auth_urls = [
    path('token/', TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]

urlpatterns = router.urls + auth_urls
