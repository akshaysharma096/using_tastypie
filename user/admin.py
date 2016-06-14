from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from user.models import Entry

admin.site.register(Entry)