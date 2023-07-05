from datetime import date

from django.contrib import admin
from django.db.models import Count, Sum

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import *


class ProductModelResource(resources.ModelResource):

    class Meta:
        model = ProductModel

        fields = (
            "id",
            "name",
            "stock",
            "description"
        )

        skip_unchanged = True


class OrderModelResource(resources.ModelResource):

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

        skip_unchanged = True


class OrderDetailsModelResource(resources.ModelResource):

    class Meta:
        model = OrderDetailsModel

        fields = (
            "id",
            "product",
            "product_order",
            "amount",
            "order"
        )

        skip_unchanged = True


@admin.register(ProductModel)
class ProductModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = ProductModelResource

    product_model_list = (
        "id",
        "name",
        "stock",
        "price"
    )

    list_display = (
        *product_model_list,
    )

    list_display_links = (
        *product_model_list,
    )

    ordering = (
        *product_model_list,
    )

    fieldsets = (
        (
            "Product info", {
                "fields": (
                    "name",
                    "stock",
                    "price",
                    "description"
                )
            }
        ),
        (
            "Product position", {
                "fields": (
                    "order",
                )
            }
        ),
        (
            None, {
                "fields": (
                    "created",
                    "updated"
                )
            }
        ),
    )

    readonly_fields = (
        "created",
        "updated"
    )


class OrderDetalsModelInline(admin.TabularInline):
    model = OrderDetailsModel
    extra = 1
    readonly_fields = ('created',)


@admin.register(OrderModel)
class OrderModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = OrderModelResource

    inlines = [OrderDetalsModelInline]

    order_model_list = (
        "id",
        "client",
        "date_order",
        "state",
        "paid",
        "shipping_rule"
    )

    list_display = (
        *order_model_list,
    )

    list_display_links = (
        *order_model_list,
    )

    fieldsets = (
        (
            "Order info", {
                "fields": (
                    "state",
                    "paid",
                    "shipping_rule",
                    "date_order",
                    "observations"
                )
            }
        ),
        (
            "Client info", {
                "fields": (
                    "client",
                )
            }
        )
    )

    readonly_fields = (
        "created",
        "updated",
        "date_order"
    )


@admin.register(OrderDetailsModel)
class OrderDetailsModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = OrderDetailsModelResource

    order_detail_model_list = (
        "id",
        "product",
        "product_order",
        "amount"
    )

    list_display = (
        *order_detail_model_list,
    )

    list_display_links = (
        *order_detail_model_list,
    )

    readonly_fields = (
        "created",
        "updated",
        "product_order"
    )
