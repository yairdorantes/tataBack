from django.views import View
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Ventas,Products,Clients,Providers

# Create your views here.
from django.contrib.auth import authenticate

class ProductsView(View):
    def get(self,request):
        products = list(Products.objects.values())
        return JsonResponse({"products":products})
class ClientsView(View):
    def get(self, request):
        clients = list(Clients.objects.values())
        return JsonResponse({"clients": clients})
    
class ProvidersView(View):
    def get(self, request):
        providers = list(Providers.objects.values())
        return JsonResponse({"providers": providers})
 
class VentasView(View):
    def get(self, request):
        ventas = list(Ventas.objects.values())
        return JsonResponse({"ventas": ventas})

class LoginView(View):
    def post(self,request):
        jd = json.loads(request.body)
        username = jd['username']
        password = jd['password']
        user  = authenticate(username=username,password=password)
        if user is not None:
            return HttpResponse("success", status=200)
        else:
            # return JsonResponse({"status":"402"})
            return HttpResponse("Processing was unsuccess.", status=401)
        # return JsonResponse({"message":"success"})