from django.db import models
from accounts.models import User

class DeliveryInfo (models.Model):
    pickup = models.CharField(max_length=250)
    drop = models.CharField(max_length=250)
    picklat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    picklong = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    droplat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    droplong = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True)
    contact_pick = models.IntegerField(default=None, null=True)
    contact_drop = models.IntegerField(default=None, null=True)
    instructions = models.TextField(max_length=2500)
    date = models.DateField(auto_now_add=True, null=True)
    order_time = models.TimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    is_seen =  models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    user_read = models.BooleanField(default=False)
    exec_read = models.BooleanField(default=False)
    amount = models.IntegerField(default=None, null=True)
    duration_exec_pick= models.IntegerField(default=None, null=True)
    duration_pick_drop = models.IntegerField(default=None, null=True)

    def __str__(self):
        return str(self.user)

    def snippet(self):
        return self.instructions[:80] + "..."
