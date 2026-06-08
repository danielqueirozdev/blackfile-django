from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, null=False)
    content = models.TextField(max_length=100000, null=True)

    def __str__(self):
        return self.title