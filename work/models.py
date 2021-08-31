from django.db import models

class Work(models.Model):
    # user
    TOOLS_USED = (
        ('PHOTOSHOP','ADOBE PHOTOSHOP'),
        ('ILLUSTRATE','ADOBE ILLUSTRATE'),
        ('AEFFECTS','ADOBE AFTER EFFECTS'),
        ('PREMIEREPRO','ADOBE PREMIERE PRO')
    )
    title = models.CharField (max_length=150)
    tags = models.ManyToManyField('Tag', blank=True)
    tools_used = models.CharField(max_length=200, choices=TOOLS_USED)
    Cover = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

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