from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('word/deeds/<int:pk>', views.WordUpdateDestroyView.as_view()),
    path('words/', views.WordListView.as_view())
]

