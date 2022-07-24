from django.urls import path

from . import views

app_name = 'multipleimages'

urlpatterns = [
    path('multiple_images_upload/',
         views.MultipleImagesUploadView.as_view(),
         name="multiple_images_upload_url"
         ),

    path('multiple_image_list/',
         views.MultipleImageListView.as_view(),
         name="multiple_image_list_url"
         ),

    path('<int:pk>/delete_multi_image/',
         views.MultipleImageDeleteView.as_view(),
         name="multi_image_delete_url"
         ),
]
