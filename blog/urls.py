from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # Strona główna bloga. Tutaj jest lista postów
    path('', views.index, name='index'),
    # Strona z wpisami w wybranym poście
    path('post/<int:post_id>/', views.post, name='post'),
    # Strona do dodawania posta
    path('new_post/', views.new_post, name='new_post'),
    # Strona do edycji wybranego postu
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Usuwanie postu
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    # Strona do dodawania wpisu do wybranego posta
    path('new_entry/<int:post_id>/', views.new_entry, name='new_entry'),
    # Strona do edycji wybranego wpisu wybranego posta
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    # Usuwanie wpisu
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
]
