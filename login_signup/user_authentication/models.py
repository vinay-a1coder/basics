from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
