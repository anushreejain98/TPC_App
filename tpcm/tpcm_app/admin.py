from django.contrib import admin
# Register your models here.
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User
admin.site.register(User)
