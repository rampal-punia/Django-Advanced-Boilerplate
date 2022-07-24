from django.contrib import admin
from .models import MultipleImageFile


@admin.register(MultipleImageFile)
class MultipleImageFileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
