"""
URL configuration for app_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Pruebatécnica PymeDesk- ApiDoc",
        default_version='v1.0.0',
        description="Documentación de las API",
        terms_of_service=f"https://pymedesk.com/",
        contact=openapi.Contact(email="tecnologia@pymedesk.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)

admin_path = [
    path(
        'sebas:)/',
        admin.site.urls
    ),
]

third_party_paths = [
    path(
        "__debug__/",
        include("debug_toolbar.urls")
    ),
    path(
        'accounts/',
        include('rest_framework.urls')
    ),
    path(
        'api/docs/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    path(
        'api/docs/<format>/',  # example: /api/docs/.json/ or /api/docs/.yaml/
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json'
    )
]

local_apps_paths = [
    re_path(
        'api/',
        include(
            'apps.product.API.routers'
        )
    ),
    path(
        'api/',
        include(
            'apps.product.API.urls'
        )
    ),
    path(
        'api/',
        include(
            'apps.users.API.urls'
        )
    ),
]

urlpatterns = admin_path + third_party_paths + local_apps_paths + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
