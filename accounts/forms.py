from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ['birth_date','location', 'bio']
