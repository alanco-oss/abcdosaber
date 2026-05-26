from django.urls import path

from . import views


urlpatterns = [
    path('atividades', views.atividades, name='atividades')]