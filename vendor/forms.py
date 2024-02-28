from django import forms
from .models import vendor

class VendorCreationForm(forms.ModelForm):

    class Meta:
        model = vendor
        fields = ['vendor_name', 'vendor_slug', 'vendor_license']