from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

from apps.default_pagination_serializer import DefaultPaginationSerializer

from apps.users.models import UserModel
from apps.users.API.serializers import UserModelSerializer


class GeneralUserModelAPIView():
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = DefaultPaginationSerializer


class ListUserModelAPIView(GeneralUserModelAPIView, ListAPIView):
    pass


class CreateUserModelAPIView(GeneralUserModelAPIView, CreateAPIView):
    pass


class DestroyUserModelAPIView(GeneralUserModelAPIView, DestroyAPIView):
    pass


class RetrieveUserModelAPIView(GeneralUserModelAPIView, RetrieveAPIView):
    pass


class UpdateUserModelAPIView(GeneralUserModelAPIView, UpdateAPIView):
    pass
