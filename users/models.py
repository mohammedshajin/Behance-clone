from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    bio= models.TextField(blank=True, null=True)
    dp = models.ImageField(blank=True, null=True, upload_to= 'profiles/', default="profiles/download.jpeg")
    location = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    dribbble = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['is_read', '-created']

