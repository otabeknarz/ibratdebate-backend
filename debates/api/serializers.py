from rest_framework import serializers

from debates.models import Debate, Ticket
from users.api.serializers import RegionSerializer, RegionSerializerForDebate, DistrictSerializer, UserSerializer


class DebateSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Debate
        fields = '__all__'


class TicketWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    debate = DebateSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
