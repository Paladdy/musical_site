from django import forms
from my_app.models import Comment, PostStatus, KeySong
from django.core.validators import RegexValidator, EmailValidator, URLValidator





class CommentForm(forms.ModelForm):
    """Быстро и без деталей"""
    class Meta:
        model = Comment
        fields = ['body']

    author = forms.IntegerField(widget=forms.HiddenInput(), required=False)

class NewPostForm(forms.ModelForm):
    class Meta:
        model = KeySong
        fields = ['title', 'status', 'price']
        widgets = {
            'title': forms.TextInput(),
            'body': forms.Textarea(attrs={'rows': 10, 'cols': 100}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'status': forms.Select()
        }



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






