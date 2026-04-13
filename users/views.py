from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserConfirmation
from rest_framework import status
from django.contrib.auth import authenticate
import random




@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Введите имя пользователя и пароль'}, 
        status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь с таким именем уже существует'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    user.is_active = False
    user.save()

    code = ''.join(random.choices('0123456789', k=6))
    UserConfirmation.objects.create(user=user, code=code)

    return Response({'message': 'Пользователь зарегистрирован!', 
                     'code': code},
                    status=status.HTTP_201_CREATED)

@api_view(['POST'])
def confirm_view(request):
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
    

@api_view(['POST'])
def authorzation_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)

    