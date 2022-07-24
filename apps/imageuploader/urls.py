from django.urls import path

from . import views

app_name = 'imageuploader'

urlpatterns = [
    # Home page
    path('',
         views.HomeTemplateView.as_view(),
         name="home_url"
         ),

    # Single/orig image urls
    path('single_image_upload/',
         views.SingleImageUploadView.as_view(),
         name="single_image_upload_url"
         ),

    path('single_image_list/',
         views.SingleImageListView.as_view(),
         name="single_image_list_url"
         ),

    path('<int:pk>/single_image_Detail/',
         views.SingleImageDetailView.as_view(),
         name="single_image_detail_url"
         ),

    # Cropped image urls
    path('cropped_image_save/',
         views.CroppedImageSaveView.as_view(),
         name="crop_image_js_url"
         ),

    path('cropped_image_upload/',
         views.CroppedImageUploadView.as_view(),
         name="cropped_image_upload_url"
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

    # Image Group urls
    path('create_image_group/',
         views.ImageGroupCreateView.as_view(),
         name="image_group_create_url"
         ),

    path('<int:pk>/Update_image_group/',
         views.ImageGroupUpdateView.as_view(),
         name="image_group_update_url"
         ),

    path('image_group_list/',
         views.ImageGroupListView.as_view(),
         name="image_group_list_url"
         ),

    path('<int:pk>/image_group_detail/',
         views.ImageGroupDetailView.as_view(),
         name="image_group_detail_url"
         ),
]
