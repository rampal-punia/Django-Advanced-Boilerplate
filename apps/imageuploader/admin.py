from django.contrib import admin
from .models import ImageFile


@admin.register(ImageFile)
class ImageFileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
