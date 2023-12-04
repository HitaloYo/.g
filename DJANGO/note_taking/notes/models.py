from django.db import models

# Create your models here.
class Note(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=256) 
    done = models.BooleanField(default=False)
