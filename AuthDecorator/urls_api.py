from django.urls import path
from .views_api import *

urlpatterns = [
    path('user/login', user_login, name='user-login'),
    path('driver/get-view', get_driver_view, name='driver-get-view'),
]
