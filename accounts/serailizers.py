from rest_framework import serializers
from .models import Customuser

class RegisterSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Customuser
        fields = ["id","username","email","password","password2"]

    def validate(self,data):
        if data["password"] != data["password2"]:
            return serializers.ValidationError("Passwords do not match")
        return data

    def create(self,validated_data):
        validated_data.pop("password2")
        user = Customuser.objects.create(**validated_data)
        return user


class Loginserailizer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class LogoutSerailizer(serializers.ModelSerializer):
    refresh = serializers.CharField()

class RefreshSerailizer(serializers.ModelSerializer):
    refresh = serializers.CharField()

class UserProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ["id","username","email"]
