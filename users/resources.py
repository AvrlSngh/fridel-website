from import_export import resources
from .models import DeliveryInfo

class PersonResource(resources.ModelResource):
    class Meta:
        model = DeliveryInfo
