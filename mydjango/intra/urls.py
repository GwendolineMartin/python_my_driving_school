from django.urls import path
from . import views

urlpatterns = [
    path('', views.rdv_list, name='rdv_list'),
]
