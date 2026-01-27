from django.urls import path, include
from . import views

app_name = 'file_uploader'
urlpatterns = [
    path('upload_file_view/', views.upload_file_view, name='upload_file_view'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete_all_files/', views.delete_all_files, name='delete_all_files'),
]