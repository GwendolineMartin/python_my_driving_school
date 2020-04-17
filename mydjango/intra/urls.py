from django.urls import path
from . import views

urlpatterns = [
    path('', views.rdv_list, name='rdv_list'),
    path('rdv/<int:pk>/', views.rdv_detail, name='rdv_detail'),
    path('rdv/create/', views.rdv_create, name='rdv_create'),
    path('rdv/create/<int:pk>', views.rdv_detail, name='rdv_dedirectTo'),

    path('rdv/<int:pk>/edit/', views.rdv_edit, name='rdv_edit'),
<<<<<<< Updated upstream
    path('rdv/<int:pk>/remove/', views.rdv_remove, name='rdv_remove')
=======
    path('rdv/<int:pk>/remove/', views.rdv_remove, name='rdv_remove'),

    path('forfait/<int:pk>/', views.forfait_detail, name='forfait_detail'),
    path('forfait/create/', views.forfait_create, name='forfait_create'),
    path('forfait/create/<int:pk>', views.forfait_detail,
         name='forfait_dedirectTo'),

    path('forfait/<int:pk>/edit/', views.forfait_edit, name='forfait_edit'),
    path('forfait/<int:pk>/remove/', views.forfait_remove, name='forfait_remove'),

>>>>>>> Stashed changes
]
