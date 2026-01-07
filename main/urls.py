from django.urls import path
from .views import create_hubspot_contact

urlpatterns = [
    path("create-contact/", create_hubspot_contact),
]
