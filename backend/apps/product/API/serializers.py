from rest_framework import serializers

from apps.product.models import OrderDetailsModel, OrderModel, ProductModel
from apps.users.API.serializers import UserModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            "name",
            "stock",
            "price",
            "description"
        )

        read_only_fields = (
            "id",
            "created",
            "updated",
        )

class OrderDetailsModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()

    class Meta:
        model = OrderDetailsModel
        fields = (
            "id",
            "order",
            "product",
            "product_order",
            "amount"
        )

        read_only_fields = (
            "id",
            "created",
            "updated",
        )
    

class OrderModelSerializer(serializers.ModelSerializer):
    products = OrderDetailsModelSerializer(many=True)
    client = UserModelSerializer()

    class Meta:
        model = OrderModel
        fields = (
            "id",
            "client",
            "date_order",
            "state",
            "paid",
            "shipping_rule",
            "observations",
            "products"
        )

        read_only_fields = (
            "id",
            "created",
            "updated",
        )

class ResumeSerializer(serializers.Serializer):
    num_orders = serializers.IntegerField()
    num_customers = serializers.IntegerField()
    income_last_month = serializers.DecimalField(max_digits=10, decimal_places=2)
    income_current_month = serializers.DecimalField(max_digits=10, decimal_places=2)
    city_more_orders = serializers.SerializerMethodField()
    best_selling_product = serializers.SerializerMethodField()


    def get_city_more_orders(self, obj):
        if obj["city_more_orders"]:
            return obj["city_more_orders"]["client__city"]
        return None

    def get_best_selling_product(self, obj):
        if obj["best_selling_product"]:
            return obj["best_selling_product"]["products__name"]
        return None