from rest_framework import serializers

from users.models import User, Region, District


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "first_name",
            "last_name",
            "username",
            "phone",
            "age",
            "region",
            "district",
            "english_level",
            "language_code"
        )
