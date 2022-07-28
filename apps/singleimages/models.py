import os

from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension

from config.models import CreationModificationDateBase

User = settings.AUTH_USER_MODEL


class ImageFile(CreationModificationDateBase):
    '''Upload single image'''
    user = models.ForeignKey(User,
                             related_name="images",
                             on_delete=models.CASCADE
                             )
    image = models.ImageField(upload_to="images",
                              validators=[validate_image_file_extension],
                              )

    @property
    def get_imageurl(self):
        return self.image.url

    @property
    def get_imagepath(self):
        return self.image.path

    @property
    def get_filename(self):
        return os.path.split(self.image.path)[-1]

    def get_absolute_url(self):
        return reverse_lazy("singleimages:single_image_detail_url", kwargs={"pk": self.pk})
