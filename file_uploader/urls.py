from django.urls import path, include
from . import views

app_name = 'file_uploader'
urlpatterns = [
    path('add_file/', views.add_file, name='add_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
]