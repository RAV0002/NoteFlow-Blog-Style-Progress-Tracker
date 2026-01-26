from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'
urlpatterns = [
    # Domyślne adresu URL uwierzytelniania
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji nowego użytkownika
    path('register/', views.register, name='register'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)