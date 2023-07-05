from django.urls import path

from apps.product.API.views import ResumeView

urlpatterns = [
    path(
        'resumen/',
        ResumeView.as_view(),
        name="resumen"
    )
]