from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}, {self.content}, {self.creator}'


class User_view(models.Model):
    image = models.ImageField(upload_to='avatar', blank=True, null=True)
    status = models.CharField(max_length=255,  blank=True, null=True)
    quote = models.TextField()
    authorquote = models.CharField(max_length=255,  blank=True, null=True)
    instalink = models.CharField(max_length=255,  blank=True, null=True)
    telelink = models.CharField(max_length=255,  blank=True, null=True)
    gitlink = models.CharField(max_length=255,  blank=True, null=True)

    def __str__(self):
        return f'{self.status}, {self.quote}'