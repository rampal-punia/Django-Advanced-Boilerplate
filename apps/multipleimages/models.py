import os

from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


User = settings.AUTH_USER_MODEL


class MultipleImageFile(models.Model):
    '''Upload Multiple images using django forms and models.'''

    user = models.ForeignKey(User,
                             related_name="multi_images",
                             on_delete=models.CASCADE
                             )

    image = models.ImageField(upload_to="images")

    @property
    def get_imageurl(self):
        return self.image.url

    @property
    def get_imagepath(self):
        return self.image.path

    @property
    def get_filename(self):
        return os.path.split(self.image.path)[-1]
