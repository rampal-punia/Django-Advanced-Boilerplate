from django.urls import path
from . import views

app_name = 'dropzoneimages'

urlpatterns = [
    path('create_image_set/', views.ImageSetCreateView.as_view(),
         name='imageset_create_url'),

    path('image_set_list/', views.ImageSetListView.as_view(),
         name='imageset_list_url'),

    path('<int:pk>/imageset/', views.ImageSetDetailView.as_view(),
         name='imageset_detail_url'),

    path('<int:pk>/upload_images/', views.DzImagesUploadView.as_view(),
         name='upload_images_url'),

    path('<int:pk>/images_list/', views.DzImagesListView.as_view(),
         name='images_list_url'),

    path('<int:imgset_pk>/delete_image/<int:pk>/', views.DzImagesDeleteUrl.as_view(),
         name='dz_image_delete_url'),
]
