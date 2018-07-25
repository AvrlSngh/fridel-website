from django import forms
from executive import models

class GetExec_Location(forms.ModelForm):
    class Meta:
        model = models.ExecutiveInfo
        fields = ['Locationlat', 'Locationlong', 'live_location', 'Amount', 'Duration', 'Duration_pick_drop']
