from django.contrib.auth.models import User
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','email','password']
        extra_kwargs={"password": {"write_only": True}}
        
        def create(self,validated_data):
            user= User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user