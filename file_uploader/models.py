from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/%Y_%m_%d')
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name