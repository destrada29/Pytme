from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from apps.product.API.views import OrderDetailsModelViewSet, ResumeView

router = DefaultRouter()

router.register(
    r"pedidos",
    OrderDetailsModelViewSet,
    basename="pedidos"
)

urlpatterns = router.urls