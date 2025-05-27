from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("debates", views.DebateViewSet)
router.register("tickets", views.TicketViewSet)

urlpatterns = router.urls
