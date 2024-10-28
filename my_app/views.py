from lib2to3.fixes.fix_input import context
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from my_app.models import KeySong, PostStatus, Product
from .forms import PriceFilterForm, CommentForm


#------Вывод всех постов-экземпляров из Бд--------
def song_list(request):

    """Получи экземпляры только PUBLISHED"""

    songs = KeySong.objects.filter(status__code='PB')
    return render(request, 'my_app/song/list.html', context={'songs': songs}) #отправляем посты на отрисовку в темплейте
#--------------------------------------------------


#------Вывод деталей поста-----------
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
        comment.save() # Сохраняем комментарий в БД


    return render(request, template_name='my_app/song/comment.html',
                  context={'song': song,
                           'form': form,
                           'comment': comment})



def home(request):

    """Главная страница сайта"""

    return render(request, 'my_app/main_page/home.html')


def products_list(request):

    """Фильтр по цене"""

    song = KeySong.objects.filter(status__code='PB') #Тут изначально Product.objects !!!! KeySong.objects.all()
    form = PriceFilterForm(request.GET) # Форма обработки и валидации данных

    if form.is_valid():
        min_price = form.cleaned_data['min_price'] #используем метод к форме для валидации данных, для получения из словаря cleaned_data минимальной цены и макс
        max_price = form.cleaned_data['max_price']

    if min_price is not None:
        song = song.filter(price__gte=min_price)  # Фильтр по минимальной цене
    if max_price is not None:
        song = song.filter(price__lte=max_price)  # Фильтр по максимальной цене

    context = {
        'song': song,
        'form': form,
    }

    return render(request, 'my_app/product/product_list.html', context)