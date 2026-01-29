from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'files/user_{instance.owner.username}/{filename}'

# Create your models here.
class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=user_directory_path)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name