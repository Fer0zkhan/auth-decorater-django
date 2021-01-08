from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from auth_decorators.utils import *
from .utils import *


@api_view(['POST'])
def user_login(request):
    user_login_serializer = LoginSerializer(data=request.data)
    if user_login_serializer.is_valid():
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            user_profile = UserProfile.objects.get(user=user)
            user_profile_serializer = UserProfileSerializer(user_profile)
            response = {
                'user_profile': user_profile_serializer.data
            }
            return Response(success_response(response, 'User Successfully Login!'))
        else:
            return Response(data=failure_response(errors={'user': ['Invalid Username/Password!']},
                                                  msg='Invalid username or password'),
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(failure_response(user_login_serializer.errors, 'Something went wrong'))
