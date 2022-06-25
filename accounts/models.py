from django.contrib.auth.models import User
from django.db import models

from .constants import USER_CATEGORY


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.TextField(choices=USER_CATEGORY, default="NE")

    def __str__(self):
        return '%s - %s' % (self.user, self.category)
