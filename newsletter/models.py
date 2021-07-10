from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(
        null=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email
