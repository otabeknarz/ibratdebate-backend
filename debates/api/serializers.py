from rest_framework import serializers

from debates.models import Debate, Ticket
from users.api.serializers import RegionSerializer, DistrictSerializer, UserSerializer


class DebateSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    district = DistrictSerializer()
    class Meta:
        model = Debate
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'
