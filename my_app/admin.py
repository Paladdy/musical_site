from django.contrib import admin
from my_app.models import KeySong, PostStatus

@admin.register(KeySong)
class KeySongAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'published','created', 'updated','slug']
    list_filter = ['price', 'created', 'updated']
    search_fields = ['title', 'description'] #поисковая строка
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-published']

@admin.register(PostStatus)
class PostStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']



# Register your models here.
