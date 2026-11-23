from rest_framework import serializers
from .models import Customuser

class RegisterSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Customuser
        