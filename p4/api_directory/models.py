from django.db import models

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    archivo = models.FileField(blank=False, null=False, upload_to='media')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

