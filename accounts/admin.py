from django.contrib import admin
from .models import User, order_id_count

admin.site.register(User)
admin.site.register(order_id_count)
