from django.urls import path

from apps.users.API.views import (
    ListUserModelAPIView,
    CreateUserModelAPIView,
    DestroyUserModelAPIView,
    RetrieveUserModelAPIView,
    UpdateUserModelAPIView
)

urlpatterns = [
    path(
        'usuarios/listar/',
        ListUserModelAPIView.as_view(),
        name="usuarios"
    ),
    path(
        'usuarios/crear/',
        CreateUserModelAPIView.as_view(),
        name="usuarios"
    ),
    path(
        'usuarios/eliminar/<pk>/',
        DestroyUserModelAPIView.as_view(),
        name="usuarios-eliminar"
    ),
    path(
        'usuarios/listar/<pk>/',
        RetrieveUserModelAPIView.as_view(),
        name="usuarios-listar"
    ),
    path(
        'usuarios/actualizar/<pk>/',
        UpdateUserModelAPIView.as_view(),
        name="usuarios-actualizar"
    )
]
