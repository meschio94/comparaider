from django.db import models
from showcase.models import Glider
from members.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class GliderReview(models.Model):
    glider = models.ForeignKey(Glider, on_delete=models.CASCADE, related_name='glider_review')
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'glider'],
                name="a user can have only one review per glider", )
        ]

    def __str__(self):
        return f"{self.glider} - {self.user}"