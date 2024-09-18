from django.urls import path
from .views import checkout_session_view, checkout_webhook_view

urlpatterns = [
    path('checkout/session/', checkout_session_view, name='checkout-session'),
    path('checkout/webhook/', checkout_webhook_view, name='checkout-webhook'),
]