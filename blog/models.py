from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """Post do którego będą dodawane wpisy"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    """Wpis do posta"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."