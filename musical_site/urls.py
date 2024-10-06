"""
URL configuration for musical_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from my_app.views import home, products_list, song_post_detail, song_list
from django.conf.urls.static import static
from django.conf import settings

#тут диспетчер смотрит откуда приходит запрос

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('songs/', products_list, name='products_list' ),

    # path('products/', products_list, name='products_list'),
    # path('post_detail/', , name='post_detail'),


    # path('my_app/', include('my_app.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('my_app/', include('my_app.urls', namespace='my_app')),
    # path('', lambda request: redirect('login')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
