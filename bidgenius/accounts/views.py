from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated  
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework_simplejwt.authentication import JWTAuthentication


import random
import string


User = get_user_model()

class ListAdminUsersView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self, request, user_id=None):
        if user_id:
            try:
                user = User.objects.get(pk=user_id, role='admin')
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'Admin user not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.filter(role='admin')
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        

def generate_password(length=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits 
    password = ''.join(random.choice(chars) for i in range(length))
    return password

class CreateAdminUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            user.role = 'admin'  
            password = generate_password()  
            user.set_password(password)
            user.save()  
   
              
            send_mail(
                        subject="Welcome to BidGenius!",
                        message=f"Hi {user.username},\nYour account has been created successfully.\nYour password is: {password}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[user.email],
                    )
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': ' "admin" role can be created.'}, status=status.HTTP_400_BAD_REQUEST)
      


class AdminVerifyView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == 'admin':
                return Response({'message': 'User is an admin.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User is not an admin.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)



class LoginVerifyView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_authenticated:
                if user.role == 'admin':
                    return Response({'message': 'User is an admin.', 'role': 'admin'}, status=status.HTTP_200_OK)
                elif user.role == 'user':
                    return Response({'message': 'User is a regular user.', 'role': 'user'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'User role is undefined.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'User is not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
