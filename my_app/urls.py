from django.urls import path
from my_app.views import song_post_detail




app_name = 'musical_site'

urlpatterns = [
    path('/<int:id>/',song_post_detail, name='song_post_detail'),
]