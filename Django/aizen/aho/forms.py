from django import forms
from .models import hostel
class hostel_form(forms.ModelForm):
    class Meta:
        model=hostel
        fields="__all__"