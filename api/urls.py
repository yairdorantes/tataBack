from django.urls import path
from .views import LoginView, ProductsView, ClientsView, ProvidersView, VentasView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login', csrf_exempt(LoginView.as_view()), name="login"),
    path('products', csrf_exempt(ProductsView.as_view()), name="products"),
    path('clients', csrf_exempt(ClientsView.as_view()), name="clients"),
    path('providers', csrf_exempt(ProvidersView.as_view()), name="providers"),
    path('ventas', csrf_exempt(VentasView.as_view()), name="ventas"),
]
