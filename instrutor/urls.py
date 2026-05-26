from django.urls import path

from . import views

urlpatterns = [path('instrutor', views.instrutor, name='instrutor'),]