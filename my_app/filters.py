import django_filters
from django import forms
from .models import Product, KeySong

MIN_PRICE = 0
MAX_PRICE = 10000

class SearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название',
                                    field_name='name',
                                    lookup_expr='icontains',
                                    required=False,
                                    widget=forms.TextInput(attrs={'class': 'filter'}))

    min_price = django_filters.NumberFilter(label='Минимальная цена',
                                           field_name='price',
                                           lookup_expr='gte',
                                           required=False,
                                           widget=forms.NumberInput(attrs={'class': 'filter'}))

    max_price = django_filters.NumberFilter(label='Максимальная цена',
                                            field_name='price',
                                            lookup_expr='lte',
                                            required=False,
                                            widget=forms.NumberInput(attrs={'class': 'filter'}))

    class Meta:
        model = KeySong
        fields = ['title', 'min_price', 'max_price']
