from django.urls import path

from . import views
# untuk Admin, URL selalu memakai prefix admindir/
# agar tidak terjadi konflik dengan manager
# kalau ada saran prefix lain boleh banget diganti ndre
urlpatterns = [
    path('', views.index, name='index'),
    path('datamaster/cabang/', views.data_master_cabang, name='datamaster'),
    path('datamaster/pengguna/', views.data_master_pengguna, name= 'datamaster'),
    path('datamaster/bank/', views.data_master_bank),
    path('datamaster/pelanggan/', views.data_master_pelanggan),
    path('monitoring/', views.monitoring,name='monitoring'),
    path('admindir/', views.admin_index, name='admin_index'),
    path('admindir/penjualan/', views.admin_penjualan),
    path('admindir/piutang/', views.admin_piutang),
    path('admindir/addpenjualan/', views.admin_addPenjualan),
    path('admindir/piutangpelanggan/', views.admin_piutangpelanggan),
    path('admindir/piutangpelanggan/add/', views.admin_add_piutang),
    path('admindir/invoice/', views.admin_invoice),
    path('admindir/pelunasan/', views.admin_pelunasan)
]