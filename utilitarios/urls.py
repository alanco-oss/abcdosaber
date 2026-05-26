from django.urls import path

from . import views


urlpatterns = [path('utilitarios', views.utilitarios, name='utilitarios')
]