from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    elements = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Word(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    time = models.DateTimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.word} {self.translation}"

