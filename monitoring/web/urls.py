from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datamaster/cabang/', views.data_master_cabang, name='datamaster'),
    path('datamaster/pengguna', views.data_master_pengguna, name= 'datamaster'),
    path('monitoring', views.monitoring,name='monitoring')
]