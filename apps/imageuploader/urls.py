from django.urls import path

from . import views

app_name = 'imageuploader'

urlpatterns = [
    path('', views.ImageUploadView.as_view(), name="image_upload_url")
]
