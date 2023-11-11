"""
URL configuration for ShoeStores project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ShoeStores import settings
from shoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-url'),
    path('cart/',views.cart, name='cart-url'),
    path('payment/', views.payment, name='payment-url'),
    path('add_to_cart/<int:shoe_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.view_cart, name='cart-url'),
    path('', include('shoes.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)