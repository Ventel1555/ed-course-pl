from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect

class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Автоматический вход после регистрации
            return Response({
                'message': 'User registered successfully',
                'user': {'username': user.username, 'email': user.email, 'role': user.role}
            }, status=status.HTTP_201_CREATED)
        return Response({
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response({
                    'message': 'Login successful',
                    'user': {'username': user.username, 'email': user.email, 'role': user.role}
                }, status=status.HTTP_200_OK)
            return Response({
                'errors': {'non_field_errors': ['Invalid credentials']}
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterHTMLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'users/register.html')

class UserLoginHTMLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'users/login.html')

class UserLogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class UserLogoutHTMLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logout(request)
        return redirect('/users/login/')