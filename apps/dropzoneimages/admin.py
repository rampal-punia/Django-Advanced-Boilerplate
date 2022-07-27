from django.contrib import admin
from .models import ImageSet, ImagesUpload


@admin.register(ImageSet)
class ImageSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'user']


@admin.register(ImagesUpload)
class ImagesUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_set', 'image']
