from django.contrib import admin

# Register your models here.
from .models import Contact, UserProfile

admin.site.register(Contact)
admin.site.register(UserProfile)