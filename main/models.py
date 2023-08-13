from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class Unit(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    elements = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Word(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    time = models.DateTimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.word} {self.translation}"



# @receiver(post_save, sender=Word)
# @receiver(pre_delete, sender=Word)
# def update_unit_elements(sender, instance, **kwargs):
#     if kwargs.get('created', False):
#         unit = instance.unit
#         unit.elements += 1
#     else:
#         unit = instance.unit
#         unit.elements -= 1
#     unit.save()

