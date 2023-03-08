from django.contrib import admin
from .models import Ventas,Products,Clients,Providers

admin.site.register([Ventas,Products,Clients,Providers])
