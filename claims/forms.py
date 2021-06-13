from django import forms
from django.forms import ModelForm
from .models import Claim

class ClaimForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClaimForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['email'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['mobile_no'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['vehicle_year_make'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['vehicle_model'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['vehicle_no'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['date_and_time'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['location'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['type_of_loss'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['description_loss'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['police_report_lodged'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['anybody_injured'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['photo'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
        # self.fields['cover_note'].widget.attrs = {
        #     'class': 'form-control col-md-6'
        # }
    class Meta:
        model = Claim
        fields = ['user','name','email','mobile_no','vehicle_year_make','vehicle_model','vehicle_no','date_and_time','location','type_of_loss','description_loss','police_report_lodged','anybody_injured','photo','cover_note']
        #fields = ('name','photo','cover_note')
        #fields = ['name','mobile_no','vehicle_model']  