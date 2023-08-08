from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework import generics, filters
from datetime import timedelta, datetime
from rest_framework.response import Response


class HomeView(generics.ListAPIView):
    serializer_class = serializers.WordSerializer
    def get_queryset(self):
        seven_days_ago = datetime.now() - timedelta(days=7)
        words = models.Word.objects.filter(unit__owner = self.request.user,time__day = seven_days_ago.day, time__month = seven_days_ago.month)
        
        return words
    

class WordListView(generics.ListAPIView):
    serializer_class = serializers.WordSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['word', 'translation']

    def get_queryset(self):
        words = models.Word.objects.filter(unit__owner=self.request.user)
        return words


class WordUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.all()

    






