from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from my_app.models import KeySong, PostStatus, Product
from .forms import PriceFilterForm

def song_post_detail(request, id):
    post = get_object_or_404(PostStatus, id=id)
    return render(request, template_name='my_app/song/list.html', context={'songs': songs})
    """shortcut для выдачи 404 ошибки"""

def song_list(request): #работаем с запросом пользователя по http
    songs = KeySong.objects.filter(status__code='PB') #ORM-method #select * from KeySong where status published / # сохраняем фильтр с постами в songs
    #return render(request, template_name='my_app/song/list.html', context={'songs': songs})
    return render(request, 'my_app/song/list.html') #отправляем посты на отрисовку в темплейте

def home(request):
    return render(request, 'my_app/main_page/home.html')

def products_list(request):
    products = Product.objects.all()
    form = PriceFilterForm(request.GET)

    if form.is_valid():
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']

    if min_price is not None:
        products = products.filter(price__gte=min_price)  # Фильтр по минимальной цене
    if max_price is not None:
        products = products.filter(price__lte=max_price)  # Фильтр по максимальной цене

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'my_app/product/product_list.html', context)