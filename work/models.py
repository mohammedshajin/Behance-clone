
from typing import Text
from django.db import models
from users.models import Profile

class Work(models.Model):
    profile= models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField (max_length=150)
    tags = models.ManyToManyField('Tag', blank=True)
    tools_used = models.ManyToManyField('Tools', blank=True)
    Cover = models.ImageField(upload_to='media')
    imageone = models.ImageField(upload_to='media', null=True, blank=True)
    imagetwo = models.ImageField(upload_to='media', null=True, blank=True)


    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tools(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    coment_date=models.DateTimeField(auto_now_add=True)

class Appreciate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)