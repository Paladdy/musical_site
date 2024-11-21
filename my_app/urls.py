from django.urls import path
from my_app import views
from django_filters.views import FilterView
from my_app.models import KeySong



app_name = 'musical_site'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('', FilterView.as_view(model=KeySong), name="song_list_filter"),
    path('<int:year>/<slug:slug>/', views.song_post_detail, name='song_post_detail'),
    path('<int:song_id>/comment', views.post_comment, name='post_comment'),
    path('new-post/', views.new_post_view, name='new_post'), #пост пользователем
    path('practica', views.test_view, name='test_view'),
]