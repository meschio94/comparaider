from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from showcase.models import Maker

# Create your models here.

def get_upload_person_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format("User","Person",instance.id,"avatar", filename)


class User(AbstractUser):
    email = models.EmailField(_('email address'),blank=False,unique=True)
    is_person = models.BooleanField(default=True)
    is_manufacturer = models.BooleanField(default=False)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #username = models.CharField(max_length=250)
    #personImage = models.ImageField(upload_to= get_upload_person_image, default=None)
