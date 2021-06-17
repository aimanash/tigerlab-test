from django import forms

from .models import Claim


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['name', 'email', 'mobile_no', 'vehicle_year_make', 'vehicle_model',
                  'vehicle_no', 'date_and_time', 'location', 'type_of_loss', 'description_loss',
                  'police_report_lodged', 'anybody_injured', 'photo', 'cover_note']
