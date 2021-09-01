from django.db import models
import uuid

class Work(models.Model):
    # user
    title = models.CharField (max_length=150)
    tags = models.ManyToManyField('Tag', blank=True)
    tools_used = models.ManyToManyField('Tools', blank=True)
    Cover = models.ImageField(upload_to='media')
    # id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=True)

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
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    # user=
    Comment = models.TextField()
    coment_date=models.DateTimeField(auto_now_add=True)

class Appreciate(models.Model):
    # user
    work = models.ForeignKey(Work, on_delete=models.CASCADE)