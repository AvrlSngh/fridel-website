from django.db import models
from accounts.models import User
from aibl.choices import *

class DeliveryInfo (models.Model):
    package_content = models.CharField(max_length=100, choices=package_content_choices, default='Documents Or Books')
    other_package_content = models.CharField(max_length=150, null=True, blank=True)
    pickup = models.CharField(max_length=250)
    drop = models.CharField(max_length=250)
    pickup_home_number = models.IntegerField(default=None, null=True, blank=True)
    pickup_landmark = models.CharField(max_length=250, default=None, null=True, blank=True)
    drop_home_number = models.IntegerField(default=None, null=True, blank=True)
    drop_landmark = models.CharField(max_length=250, default=None, null=True, blank=True)
    picklat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    picklong = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    droplat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    droplong = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    contact_pick = models.IntegerField(default=None, null=True)
    contact_drop = models.IntegerField(default=None, null=True)
    instructions = models.CharField(max_length=250, blank=True)
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
    other_task = models.BooleanField(default=False)
    task_detail = models.TextField(max_length=6000, default=None, null=True)

    def __str__(self):
        return str(self.user)

    def snippet(self):
        return self.instructions[:80] + "..."

# class OtherTask (models.Model):
#     task_detail = models.TextField(max_length=6000)
#     date = models.DateField(auto_now_add=True, null=True)
#     order_time = models.TimeField(auto_now_add=True, null=True)
#     user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.user)
