from django.urls import path

from . import views

app_name = 'imageuploader'

urlpatterns = [
    path('',
         views.HomeTemplateView.as_view(),
         name="home_url"
         ),

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
]
