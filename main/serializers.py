from rest_framework import serializers
from . import models


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = '__all__'



