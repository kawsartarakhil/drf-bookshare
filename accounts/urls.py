from django.urls import path
from .views import *

urlpatterns = [
    path("register/",RegisterView),
    path("login/",LoginView)
]
