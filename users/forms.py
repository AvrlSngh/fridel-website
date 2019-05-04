from django import forms
from users import models

class GetPickupDrop(forms.ModelForm):
    class Meta:
        model = models.DeliveryInfo
        fields = ['pickup','pickup_home_number', 'pickup_landmark', 'contact_pick', 'drop', 'drop_home_number', 'drop_landmark',
                    'contact_drop', 'package_content','other_package_content', 'instructions', 'picklat', 'picklong', 'droplat', 'droplong']

class ExecutiveSeen(forms.ModelForm):
    class Meta:
        model = models.DeliveryInfo
        fields = ['is_seen']

class OtherTasksForm(forms.ModelForm):
    class Meta:
        model = models.DeliveryInfo
        fields = ['task_detail','other_task']


























# class AddressForm(forms.Form):
#     pickup = forms.CharField(max_length = 250)
#     drop = forms.CharField(max_length=250)
#     instructions = forms.CharField(
#         max_length = 3000,
#         widget = forms.Textarea(),
#         help_text = 'Write your instructions to our delivery boy. Keep it short and simple to understand'
#     )
#
#     def clean(self):
#         cleaned_data = super(AddressForm, self).clean()
#         pickup = cleaned_data.get('pickup');
#         drop = cleaned_data.get('drop')
#         instructions = cleaned_data.get('instructions')
#         if not pickup and not drop and not message:
#             raise forms.ValidationError('You have to fill all the fields!')
