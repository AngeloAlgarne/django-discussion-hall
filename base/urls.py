from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('edit-room/<str:pk>/', views.editRoom, name="edit-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]
