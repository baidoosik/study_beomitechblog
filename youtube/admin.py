from django.contrib import admin
from .models import Youtube
# Register your models here

@admin.register(Youtube)
class YoutubeModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','url']
    list_display_links = ['id','title']