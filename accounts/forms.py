from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ['birth_date','location', 'bio']
         widgets = {'birth_date': forms.DateInput(attrs={'class': 'datepicker'}),}

         #вот тут добавить поле first name и last name
