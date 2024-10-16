from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from my_app.models import KeySong, PostStatus, Product
from .forms import PriceFilterForm

def song_post_detail(request, year, slug):

    """Выдай объект или если нет - 404 ошибку"""

    song = get_object_or_404(KeySong, slug=slug, published__year=year)
    return render(request, 'my_app/song/detail.html', {'song': song})




def song_list(request):

    """Получи экземпляры только PUBLISHED"""

    songs = KeySong.objects.filter(status__code='PB')
    return render(request, 'my_app/song/list.html', context={'songs': songs}) #отправляем посты на отрисовку в темплейте

def home(request):

    """Главная страница сайта"""

    return render(request, 'my_app/main_page/home.html')



# def products_list(request):
#
#     """Фильтр по цене"""
#
#     song = KeySong.objects.filter(status__code='PB') #Тут изначально Product.objects !!!! KeySong.objects.all()
#     form = PriceFilterForm(request.GET) # Форма обработки и валидации данных
#
#     if form.is_valid():
#         min_price = form.cleaned_data['min_price'] #используем метод к форме для валидации данных, для получения из словаря cleaned_data минимальной цены и макс
#         max_price = form.cleaned_data['max_price']
#
#     if min_price is not None:
#         song = song.filter(price__gte=min_price)  # Фильтр по минимальной цене
#     if max_price is not None:
#         song = song.filter(price__lte=max_price)  # Фильтр по максимальной цене
#
#     context = {
#         'song': song,
#         'form': form,
#     }
#
#     return render(request, 'my_app/product/product_list.html', context)