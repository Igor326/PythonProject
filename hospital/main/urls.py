
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name='main'),
   path('about-us', views.about, name='about'),
   path('create',views.create, name = 'create'),
   path('createSpec', views.createSpec, name='createSpec'),
   path('createDisease', views.createDis, name='createDis'),
   path('createPat', views.createPat, name='createPat'),
   path('createDoc', views.createDoc, name='createDoc'),
   path('createDiag', views.createDiag, name='createDiag'),
   path('deleteSpec/<int:id>/', views.deleteSpec),
   path('deleteDis/<int:id>/', views.deleteDis),
   path('deletePat/<int:id>/', views.deletePat),
   path('deleteDoc/<int:id>/', views.deleteDoc),
   path('deleteDiag/<int:id>/', views.deleteDiag)

]
