from django.urls import path
from . import views

app_name = 'peta'

urlpatterns = [
    path('', views.LihatRestoran, name='Semua_Restoran'),
    path('create', views.createRestoran, name='buat_restoran'),
    path('simpan', views.simpan, name='simpan'),
    path('delete/<int:id>', views.deleteRestoran, name='delete'),
    path('update/<int:id>', views.updateRestoran, name='update'),
    path('edit/<int:id>', views.update, name='edit')
]