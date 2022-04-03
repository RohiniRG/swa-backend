from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    