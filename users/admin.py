from django.contrib import admin
from .models import Profile, Message, Follow

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Follow)
