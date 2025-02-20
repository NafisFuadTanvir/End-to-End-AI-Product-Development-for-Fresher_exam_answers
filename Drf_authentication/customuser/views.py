from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics,status
from .serializers import Userserializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserSignup(generics.CreateAPIView):
    serializer_class= Userserializer
    
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": serializer.data,
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED
        )

class Userlogin(generics.GenericAPIView):
    serializer_class=Userserializer
    permission_classes=[IsAuthenticated]
    def post(self,request):
        username=request.data.get('username')
        email= request.data.get('email')
        password= request.data.get('password')
        
        if not email or not password:
            return Response(
                {"details":"creadentials not valid"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        db_user= User.objects.filter(username=username).first()
        if not db_user:
            return Response(
                {"details":"creadentials not valid"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        matched_password= db_user.check_password(password)
        
        if not matched_password:
            return Response(
                {"details":"creadentials not valid"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        if not db_user.is_verified:
            return Response(
                {"details":"email is not yet verified"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        refresh= RefreshToken.for_user(db_user)
        
        return Response(
            {
                "refresh_token":str(refresh),
                "access_token":str(refresh.access_token)
            }
        )        