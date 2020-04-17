from django.urls import path
from . import views

urlpatterns = [
    path('', views.rdv_list, name='rdv_list'),
    path('rdv/<int:pk>/', views.rdv_detail, name='rdv_detail'),
    path('rdv/create/', views.rdv_create, name='rdv_create'),
    path('rdv/create/<int:pk>', views.rdv_detail, name='rdv_dedirectTo'),

    path('rdv/<int:pk>/edit/', views.rdv_edit, name='rdv_edit'),
    path('rdv/<int:pk>/remove/', views.rdv_remove, name='rdv_remove'),


]
