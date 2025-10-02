from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Domyślne adresu URL uwierzytelniania
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji nowego użytkownika
    path('register/', views.register, name='register'),
    
]
