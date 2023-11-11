from django.urls import path, include
from django_daraja import mpesa, urls

from . import views
from .models import mpesa_callback


urlpatterns = [
    path('payment/', views.payment, name='payment-url'),
    path('mpesa-callback/', mpesa_callback, name='mpesa-callback')

]
