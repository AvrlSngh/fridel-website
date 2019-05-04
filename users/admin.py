from django.contrib import admin
from .models import DeliveryInfo
from import_export.admin import ImportExportModelAdmin

admin.site.register(DeliveryInfo)
class PersonAdmin(ImportExportModelAdmin):
    pass
