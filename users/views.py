from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserConfirmation
import random


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        user.is_active = False
        user.save()

        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        UserConfirmation.objects.create(user=user, code=code)

        return Response({'message': 'Пользователь зарегистрирован!', 'code': code}, 
                        status=status.HTTP_201_CREATED)


class ConfirmView(APIView):
    def post(self, request):
        code = request.data.get('code')

        try:
            confirmation = UserConfirmation.objects.get(code=code)
            user = confirmation.user
            user.is_active = True
            user.save()
            confirmation.delete()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Пользователь подтвержден', 'token': token.key}, 
                            status=status.HTTP_200_OK)
        except UserConfirmation.DoesNotExist:
            return Response({'error': 'Неверный код подтверждения'}, 
                            status=status.HTTP_400_BAD_REQUEST)


class AuthorizationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)