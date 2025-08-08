from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from debates.api.serializers import DebateSerializer, TicketReadSerializer, TicketWriteSerializer
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
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_fields = ("debate", "debate__region", "debate__district", "user", "is_checked")
    ordering_fields = ("created_at", "is_checked")

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TicketReadSerializer
        return TicketWriteSerializer

    @action(detail=False, methods=["get", "post"])
    def stats(self, request):
        region = request.query_params.get("region")
        district = request.query_params.get("district")
        if region and district:
            tickets = Ticket.objects.filter(debate__region_id=region, debate__district_id=district)
        elif region:
            tickets = Ticket.objects.filter(debate__region_id=region)
        elif district:
            tickets = Ticket.objects.filter(debate__district_id=district)
        else:
            tickets = Ticket.objects.all()
        all_count = tickets.count()
        has_come_count = tickets.filter(is_checked=True).count()
        return Response({"all_count": all_count, "has_come_count": has_come_count}, status=200)
