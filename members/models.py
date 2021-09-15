from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_upload_person_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format("User","Person",instance.id,"avatar", filename)


class User(AbstractUser):
    email = models.EmailField(_('email address'),blank=False)
    device = models.CharField(max_length=200, null=True, blank=True)
    is_person = models.BooleanField(default=True)
    is_manufacturer = models.BooleanField(default=False)

    def __str__(self):
        if self.username:
            username = self.username
        else:
            username = self.device
        return str(username)
