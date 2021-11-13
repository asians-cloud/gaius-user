from django.urls import path

from .views import check_sso


urlpatterns = [
    path('check_sso', check_sso, name="user-check-sso"),
]

