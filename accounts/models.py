from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_executive = models.BooleanField(default=False)
    phone = models.IntegerField(default=None, null=True)
    recent_order_id = models.IntegerField(default=0, null=True)


class order_id_count(models.Model):
    count_id = models.IntegerField(default=0, null=True)
