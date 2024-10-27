from django.urls import path
from my_app import views




app_name = 'musical_site'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:year>/<slug:slug>/', views.song_post_detail, name='song_post_detail'),
]