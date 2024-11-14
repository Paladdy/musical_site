from django.urls import path
from my_app import views




app_name = 'musical_site'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:year>/<slug:slug>/', views.song_post_detail, name='song_post_detail'),
    path('<int:song_id>/comment', views.post_comment, name='post_comment'),
    path('new-post/', views.new_post_view, name='new_post_view'), #пост пользователем
    path('practica', views.test_view, name='test_view'),
]