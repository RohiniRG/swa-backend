from django.db import models
from users.models import TOPICS
from users.models import User

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    tags = models.CharField(choices=TOPICS, max_length=30, blank=True, default="menstrualHealth")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_by.username} | {self.title}' 

