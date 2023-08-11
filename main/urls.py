from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('word/deeds/<int:pk>', views.WordUpdateDestroyView.as_view()),
    path('words/own/', views.OwnWordListView.as_view()),
    path('units/own/', views.OwnUnitList.as_view()),
    path('unit/deeds/<int:pk>', views.UnitUpdateDestroyView.as_view()),
    path('words/', views.GlobalWordListView.as_view()),
    path('units/', views.GlobalUnitListView.as_view()),
    path('unit/create/', views.UnitCreateView.as_view()),
    path('word/create/', views.WordCreateView.as_view())
]

