from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import timezone
from django.db.models import Count, Sum

from apps.default_pagination_serializer import DefaultPaginationSerializer

from apps.product.models import ProductModel, OrderModel, OrderDetailsModel
from apps.product.API.serializers import ProductModelSerializer, OrderDetailsModelSerializer, OrderModelSerializer, ResumeSerializer
from apps.users.models import UserModel


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = DefaultPaginationSerializer


class OrderDetailsModelViewSet(ModelViewSet):
    queryset = OrderDetailsModel.objects.all()
    serializer_class = OrderDetailsModelSerializer
    pagination_class = DefaultPaginationSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    pagination_class = DefaultPaginationSerializer


class ResumeView(APIView):
    def get(self, request):
        num_orders = OrderModel.objects.count()

        # num_customers = OrderModel.objects.values('client').distinct().count()
        num_customers = UserModel.objects.filter(is_active=True).count()

        income_last_month = OrderModel.objects.filter(
            date_order__month=(timezone.now().month - 1)
        ).aggregate(
            total_income=Sum('products__price')
        )['total_income'] or 0

        income_current_month = OrderModel.objects.filter(
            date_order__month=(timezone.now().month)
        ).aggregate(
            total_income=Sum('products__price')
        )['total_income'] or 0

        city_more_orders = (
            OrderModel.objects.values('client__city')
            .annotate(order_count=Count('id'))
            .order_by('-order_count')
            .first()
        )

        best_selling_product = (
            OrderModel.objects.values('products__name')
            .annotate(total_sales=Sum('orderdetailsmodel__amount'))
            .order_by('-total_sales')
            .first()
        )

        data = {
            "num_orders": num_orders,
            "num_customers": num_customers,
            "income_last_month": income_last_month,
            "income_current_month": income_current_month,
            "city_more_orders": city_more_orders,
            "best_selling_product": best_selling_product,
        }

        serializer = ResumeSerializer(data)
        return Response(serializer.data)
