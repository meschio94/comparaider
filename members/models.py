from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
#from showcase.models import GliderReview


def get_upload_person_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format("User","Person",instance.id,"avatar", filename)


class User(AbstractUser):
    email = models.EmailField(_('email address'),blank=False,unique=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    is_person = models.BooleanField(default=True)
    is_manufacturer = models.BooleanField(default=False)

    def __str__(self):
        if self.username:
            username = self.username
        else:
            username = self.device
        return str(username)

#class Person(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #reviews = models.ManyToManyField(GliderReview, related_name='user_reviews')
    #username = models.CharField(max_length=250)
    #personImage = models.ImageField(upload_to= get_upload_person_image, default=None)


#class Manufacturer(models.Model):
    #user = models.OneToOneField(User, related_name=models.CASCADE, primary_key=True)
    #maker = models.OneToOneField(Maker, related_name='user_manufacturer')
