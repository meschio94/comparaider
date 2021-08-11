from django.db import models

from showcase.models import Size

from members.models import User
# Create your models here.

class CompareItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"

    @property
    def get_size_items(self):
        items = self.SizeItem_set.all()
        return items


class SizeItem(models.Model):
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, related_name='size_info', blank=True, null=True)
    compareItems = models.ForeignKey(CompareItems, related_name='size_item', on_delete=models.SET_NULL, null=True)


def __str__(self):
        return f"{self.size.glider.maker.name} - {self.size.glider.name} - {self.size.size}"