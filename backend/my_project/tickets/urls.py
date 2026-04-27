from django.urls import path
from .views import create_ticket, ticket_success


urlpatterns = [
    path('create/', create_ticket, name='create_ticket'),
    path('success/', ticket_success, name='ticket_success'),
]