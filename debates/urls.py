from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("region/<str:region_id>/", views.region_view, name="region-statistics"),
    path("district/<str:district_id>/", views.district_view, name="district-statistics"),
]
