"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeTemplateView.as_view(), name="home_url"),
    path('', include('users.urls', namespace='users')),

    path('singleimages/', include("singleimages.urls", namespace="singleimages")),
    path('multipleimages/', include("multipleimages.urls", namespace="multipleimages")),
    path('croppedimages/', include("croppedimages.urls", namespace="croppedimages")),
    path('dropzoneimages/', include("dropzoneimages.urls", namespace="dropzoneimages")),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
