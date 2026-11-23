from django.shortcuts import render
from .serailizers import RegisterSerailizer,Loginserailizer,LogoutSerailizer,RefreshSerailizer,UserProfileSerailizer
from .models import Customuser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

def RegisterView(request):
    serailizer = RegisterSerailizer
    if serailizer.is_valid(raise_exception=True):
        serailizer.save()
        return Response("regisetred successfully",serailizer.data)
    return Response(serailizer.errors)

def LoginView(request):
    serializer = Loginserailizer(data=request.user)
    serializer.is_valid(raise_exception=True)
    user = authenticate(request,serializer.username,serializer.password)
    if user is not None:
        refresh = RefreshToken(user)
        return Response({
            "refresh":str(refresh),
            "access":str(refresh.access_token),
        })
    return Response({"error":"Incorrect crediantails"})

def LogoutView(request):
    serializer = LogoutSerailizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    