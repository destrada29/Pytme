from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from apps.users.models import UserModel


class UserModelResource(resources.ModelResource):
    def before_import_row(self, row, *args, **kwargs):
        row["username"] = row["username"].lower()
        row["first_name"] = row["first_name"].title()
        row["last_name"] = row["last_name"].title()

        password = row["password"]

        if "pbkdf2" not in row['password']:
            row["password"] = make_password(password)

    class Meta:
        model = UserModel
        
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "groups",
            "user_permissions",
            "is_superuser",
            "is_staff",
            "is_active",
            "phone",
            "city",
            "address"
        )
        
        skip_unchanged = True


@admin.register(UserModel)
class UserModelAdmin(ImportExportActionModelAdmin, UserAdmin):
    resource_class = UserModelResource

    list_display = (
        "order",
        "id",
        "get_full_name",
        "email",
        "username",
        "is_staff"
    )

    list_display_links = (
        "id",
        "get_full_name",
        "email",
        "username",
        "username"
    )

    ordering = (
        "order",
        "id",
        "email",
        "first_name",
        "last_name"
    )

    fieldsets = (
        (
            "User info", {
                "fields": (
                    "username",
                    "password"
                )
            }
        ),
        (
            "Personal info", {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "city",
                    "address"
                )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates", {
                "fields": (
                    "last_login",
                    "created",
                    "updated"
                )
            }
        ),
        (
            "Order", {
                "fields": (
                    "order",
                )
            }
        ),
    )

    readonly_fields = (
        "get_full_name",
        "last_login",
        "created",
        "updated"
    )

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = "Full name"
