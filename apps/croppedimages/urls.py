from django.urls import path

from . import views

app_name = 'croppedimages'

urlpatterns = [
    # Cropped image urls
    path('orig_image_upload/',
         views.OrigImageUploadView.as_view(),
         name="orig_image_upload_url"
         ),

    path('orig_images_list/',
         views.OrigImageListView.as_view(),
         name="orig_images_list_url"
         ),

    path('<int:pk>/crop_image/',
         views.OrigImageDetailView.as_view(),
         name="crop_orig_image_url"
         ),

    path('cropped_image_save/',
         views.CroppedImageSaveView.as_view(),
         name="crop_image_js_url"
         ),

    path('cropped_images_list/',
         views.CroppedImageListView.as_view(),
         name="cropped_images_list_url"
         ),

    path('<int:pk>/cropped_image/',
         views.CroppedImageDetailView.as_view(),
         name="cropped_image_detail_url"
         ),

    path('<int:pk>/delete_cropped_image/',
         views.CroppedImageDeleteView.as_view(),
         name="cropped_image_delete_url"
         ),

]
