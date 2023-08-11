from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework import generics, filters, status
from datetime import timedelta, datetime
from rest_framework.response import Response


class HomeView(APIView):

    def get_object(self):
        try:
            seven_days_ago = datetime.now() - timedelta(days=7)
            words = models.Word.objects.filter(unit__owner = self.request.user,time__day = seven_days_ago.day, time__month = seven_days_ago.month)
            return words
        except models.Word.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request):
        words = self.get_object()
        word_ser = serializers.WordSerializer(words, many = True)
        return Response(word_ser.data)
    
    def put(self, request):
        try:
            words = self.get_object()
            for i in words:
                i.time = datetime.now()
                i.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OwnWordListView(generics.ListAPIView):
    serializer_class = serializers.WordSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['word', 'translation']

    def get_queryset(self):
        words = models.Word.objects.filter(unit__owner=self.request.user)
        return words


class WordUpdateDestroyView(APIView):

    def get_object(self, pk):
        try:
            return models.Word.objects.get(pk=pk)
        except models.Word.DoesNotExist:
            raise Http404
    
    def get(self,request, pk):
        word = self.get_object(pk)
        word_ser = serializers.WordSerializer(word)
        return Response(word_ser.data)

    def put(self,request, pk):
        word = self.get_object(pk)
        word_ser = serializers.WordSerializer(word, data=request.data)
        if word_ser.is_valid():
            word_ser.save()
            return Response(word_ser.data)
        
    def delete(self,request, pk):
        word = self.get_object(pk)
        word.delete()
        return Response({'data':'updated'})
    

class OwnUnitList(generics.ListAPIView):
    serializer_class = serializers.UnitSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['title',]

    def get_queryset(self):
        unit = models.Unit.objects.filter(owner=self.request.user)
        return unit
        

class UnitUpdateDestroyView(APIView):

    def get_objects(self, pk):
        try:
            unit = models.Unit.objects.get(owner = self.request.user,pk=pk)
            return unit
        except models.Unit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        unit = self.get_objects(pk)
        unit_ser = serializers.UnitSerializer(unit)
        return Response(unit_ser.data)
    
    def put(self, request, pk):
        unit = self.get_objects(pk)
        unit_ser = serializers.UnitSerializer(unit, data = request.data)
        if unit_ser.is_valid():
            unit_ser.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        
    def delete(self, request, pk):
        unit = self.get_objects(pk)
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GlobalWordListView(generics.ListAPIView):
    serializer_class = serializers.WordSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['word', 'translation']

    def get_queryset(self):
        return models.Word.objects.filter(unit__status = True)


class GlobalUnitListView(generics.ListAPIView):
    serializer_class =  serializers.UnitSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['title', 'owner__username']

    def get_queryset(self):
        return models.Unit.objects.filter(status = True)


class UnitCreateView(APIView):

    def post(self, request):
        try:
            status_unit = request.POST.get('status')
            about = request.POST.get('about')
            title = request.POST.get('title')

            models.Unit.objects.create(
                owner = request.user,
                status = status_unit,
                about = about,
                title = title
            )
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WordCreateView(APIView):
    def post(self, request):
        # try:
            word = request.POST.get('word')
            translation = request.POST.get('translation')
            unit_id = request.POST.get('unit_id')
            description = request.POST.get('description')

            models.Word.objects.create(
                word = word,
                translation = translation,
                time = datetime.now(),
                unit = models.Unit.objects.get(id = int(unit_id)),
                description = description
            )

            return Response(status=status.HTTP_201_CREATED)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)






