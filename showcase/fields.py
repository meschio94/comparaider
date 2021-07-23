from django.db import models

#field for custom year input
class Year(models.IntegerField):

    def __init__(self, verbose_name=None, min_value=1980, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self,verbose_name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(Year, self).formfield(**defaults)