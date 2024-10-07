from django import forms

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, label="Минимальная цена", min_value=1000, decimal_places=2)
    max_price = forms.DecimalField(required=False, label="Максимальная цена", min_value=1000, decimal_places=2)
