from django import forms
from my_app.models import Comment
from django.core.validators import RegexValidator, EmailValidator, URLValidator


class CommentForm(forms.ModelForm):
    """Быстро и без деталей"""
    class Meta:
        model = Comment
        fields = ['name', 'body']



# SEX_CHOICES = [('male', 'Male'), ('female', 'Female')]
# COLOR_CHOICES = [('black', 'Black'), ('white', 'White')]
#
# class CommentForm(forms.Form):
#      """Можно похимичить"""
#     name = forms.CharField(max_length=120, min_length=3, required=True)
#     body = forms.CharField(widget=forms.Textarea, required=True) #Textarea = большой виджет
#     age = forms.IntegerField(min_value=1, max_value=100, required=True)
#     litres = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
#     age2 = forms.ChoiceField(choices=SEX_CHOICES, required=True)
#     color = forms.MultipleChoiceField(choices=COLOR_CHOICES, required=True)
#     number = forms.CharField(validators=[RegexValidator(regex=r'\+79\d{9}$', )]) # передаем Char - стрроку, так как номер телефона содержит +, а также строка неизменяемый тип



class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, label="Минимальная цена", min_value=1000, decimal_places=2)
    max_price = forms.DecimalField(required=False, label="Максимальная цена", min_value=1000, decimal_places=2)


