from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from users.models import User, Region, District
from .serializers import UserSerializer, RegionSerializer, DistrictSerializer, SetPasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get", "put", "patch", "delete"])
    def me(self, request):
        user = request.user

        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data)

        elif request.method in ["PUT", "PATCH"]:
            serializer = self.get_serializer(
                user, data=request.data, partial=(request.method == "PATCH")
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        elif request.method == "DELETE":
            user.delete()
            return Response(status=204)

        return Response({"detail": "Invalid request."}, status=400)

    @action(detail=False, methods=["post"])
    def set_password(self, request):
        self.serializer_class = SetPasswordSerializer

        user = request.user
        current_password = request.data.get("current_password")
        new_password = request.data.get("password")

        if not current_password or not new_password:
            return Response(
                {"detail": "Both 'current_password' and 'password' are required."},
                status=400,
            )

        if not user.check_password(current_password):
            return Response({"detail": "Invalid current password."}, status=400)

        user.set_password(new_password)
        user.save()
        return Response(
            {"detail": "Password has been changed successfully."}, status=200
        )


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_fields = ("debates__is_passed",)
    ordering_fields = ("created_at",)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["region", "debates__is_passed"]
    search_fields = ["name"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
