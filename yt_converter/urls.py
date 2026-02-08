from django.urls import path, include
from . import views

app_name = 'yt_converter'
urlpatterns = [
    path('converter_view/', views.converter_view, name='converter_view'),
]