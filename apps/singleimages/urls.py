from django.urls import path

from . import views

app_name = 'singleimages'

urlpatterns = [
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

    path('<int:pk>/delete_single_image/',
         views.SingleImageDeleteView.as_view(),
         name="single_image_delete_url"
         ),
]
