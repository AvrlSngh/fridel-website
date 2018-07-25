from django.db import models
from accounts.models import User
from users.models import DeliveryInfo


class ExecutiveInfo(models.Model):
    Locationlat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    Locationlong = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    executive = models.OneToOneField(User, default=None, on_delete=models.CASCADE, primary_key=True, related_name="executive_username")
    customer = models.OneToOneField(User, default=None, on_delete=models.CASCADE, primary_key=False, related_name="customer_username")
    live_location = models.CharField(max_length=100)
    Amount = models.IntegerField(default=None, null=True)
    Duration= models.IntegerField(default=None, null=True)
    Duration_pick_drop = models.IntegerField(default=None, null=True)
    order_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return str(self.executive)
