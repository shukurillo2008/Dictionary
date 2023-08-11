from rest_framework import serializers
from . import models


class UnitSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only = True , slug_field='username')
    class Meta:
        model = models.Unit
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    unit = serializers.SlugRelatedField(read_only = True ,slug_field='title')
    class Meta:
        model = models.Word
        fields = '__all__'



