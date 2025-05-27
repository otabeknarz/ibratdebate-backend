from rest_framework import serializers

from debates.models import Debate, Ticket
from users.api.serializers import RegionSerializer, DistrictSerializer


class DebateSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    district = DistrictSerializer()
    class Meta:
        model = Debate
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
