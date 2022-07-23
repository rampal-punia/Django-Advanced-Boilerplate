import os

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from . import helper


class ImageFile(models.Model):
    image = models.ImageField(upload_to="images")

    @property
    def get_imageurl(self):
        return self.image.path

    @property
    def get_filename(self):
        return os.path.split(self.image.path)[-1]

    def get_absolute_url(self):
        return reverse("imageuploader:model_detail_url", kwargs={"pk": self.pk})
