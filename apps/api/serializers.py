from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    userprofile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = User
        fields = ["id", "first_name","last_name", "username", "email", "userprofile"]