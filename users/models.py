from itertools import cycle
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Whenever a user model instance is registered in the server, with the help of a signal we generate a token
    """
    if created:
        Token.objects.create(user=instance)

TOPICS = (
    ("menstrualHeath", "Menstrual Health"),
    ("yoga", "Yoga"),
    ("skincare", "Skin Care"),
    ("fitness", "Fitness"),
    ("mentalHealth", "Mental Health"),
    ("diet", "Diet"),
    ("sleep", "Sleep"),
    ("relationships", "Relationships"),
    ("pcos", "PCOS"),
    ("sexLife", "Sex Life"),
    ("pms", "PMS")
)

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email'), max_length=254, unique=True)
    mobile_no = PhoneNumberField(null=False, blank=False, unique=True)
    interests = models.CharField(choices=TOPICS, max_length=30, blank=True, default="menstrualHealth")
    cycleDays = models.IntegerField(default=28)
    cycleLength = models.IntegerField(default=7)
    lastCycleStart = models.DateField(default='2022-01-01')

    is_consultant = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'

