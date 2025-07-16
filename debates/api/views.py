from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from debates.api.serializers import DebateSerializer, TicketSerializer
from debates.models import Debate, Ticket


class DebateViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_fields = ("region", "district", "is_passed")
    ordering_fields = ("created_at", "date", "time")


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_fields = ("debate", "debate__region", "user", "is_checked")
    ordering_fields = ("created_at", "is_checked")

    @action(detail=False, methods=["get"])
    def stats(self, request):
        tickets = Ticket.objects.all()
        all_count = tickets.count()
        has_come_count = tickets.filter(is_checked=True).count()
        return Response({"all_count": all_count, "has_come_count": has_come_count}, status=200)
