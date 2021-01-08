from django.contrib import admin
from .models import UserProfile
from auth_decorators.admin_utils import set_admin

# Register your models here.

set_admin(UserProfile, ('user_roll',), ('-id',),
          ('user_roll', 'created_at', 'updated_at'))
