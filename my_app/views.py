from lib2to3.fixes.fix_input import context
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from my_app.models import KeySong, PostStatus, Product
from .filters import SearchFilter
from .forms import CommentForm, NewPostForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from unidecode import unidecode


#------Вывод всех постов-экземпляров из Бд--------
def song_list(request):

    """Получи экземпляры только PUBLISHED"""

    songs = KeySong.objects.filter(status__code='PB')
    product_filter = SearchFilter(request.GET, queryset=songs)
    songs = product_filter.qs

    return render(request,
                  'my_app/song/list.html',
                   context={'songs': songs,
                            # 'products': products,
                            'filter': product_filter}) #отправляем посты на отрисовку в темплейте
#--------------------------------------------------




#------Вывод всех постов-----------
def song_post_detail(request, year, slug):

    """Выдай объект или если нет - 404 ошибку"""
    song = get_object_or_404(KeySong, slug=slug, published__year=year)
    comments = song.comments.all()
    form = CommentForm()
    return render(request,
                  template_name='my_app/song/detail.html',
                  context={'song': song,
                           'form': form,
                           'comments': comments})


#------Обработка только ПОСТ-запросов-------
@login_required
@require_POST
#1) Прилетает пост-запрос для БД от пользователя
def post_comment(request, song_id):

    #2) Вернет или не вернет экземпляр поста и сохранит в пост. Просто вытаскиваем наш экземпляр из модели главного поста
    song = get_object_or_404(KeySong, id=song_id) # этот post связан (переопределен) в comment.post = post, чтобы знать под каким постом какой комментарий

    #3) Сохранится в форму то, что будет отправлено пользователем
    form = CommentForm(request.POST) # на form прилетят данные, указанные в ПОСТ-запросе
    comment = None # Предполагаем, что изначально комментарий пустой, инициализируем переменную для дальнейшей проверки

    if form.is_valid():
        comment = form.save(commit=False) # пока не сохраняем в БД
        comment.song = song # .post = вызываем поле из models, = post(foreign key) указываем к какому посту данный коммент
        comment.author = request.user
        comment.save() # Сохраняем комментарий в БД


    return render(request, template_name='my_app/song/comment.html',
                  context={'song': song,
                           'form': form,
                           'comment': comment})


def test_view(request):
    return render(request, template_name='my_app/song/practica.html')


# def home(request):
#
#     """Главная страница сайта"""
#
#     return render(request, 'my_app/main_page/home.html')


@login_required
def new_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.slug = slugify(unidecode(song.title))

            """Если поле прайс отсутствует в модели, то по умолчанию значение цены равно 0"""
            if not song.price:
                song.price = 0

            song.save()
            return redirect('my_app:song_list')
    else:
        form = NewPostForm()
    return render(request, template_name='my_app/song/new_song.html', context={'form': form})



# def filter_view(request):
#     f = PriceFilterForm(request.GET, queryset=KeySong.objects.filter(status__code='PB'))
#
#     songs = f.qs




    # if f.is_valid():
    #     # Извлекаем значения из формы
    #     min_price = f.cleaned_data.get('min_price')
    #     max_price = f.cleaned_data.get('max_price')
    #
    #     # Применяем фильтрацию по цене, если указаны параметры
    #     if min_price:
    #         songs = songs.filter(price__gte=min_price)  # фильтрация по минимальной цене
    #     if max_price:
    #         songs = songs.filter(price__lte=max_price)

    return render(request, 'my_app/song/list.html', {'filter': f, 'songs': songs})











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