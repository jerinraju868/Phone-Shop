from django.urls import path
from Api import views

urlpatterns = [
    path('users/', views.getUsers),
]