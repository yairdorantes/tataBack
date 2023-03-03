from django.views import View
import json
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth import authenticate

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