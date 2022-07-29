import os

from django.db import models
from django.core.validators import validate_image_file_extension
from django.urls import reverse_lazy
from django.conf import settings

User = settings.AUTH_USER_MODEL


class OrigImageFile(models.Model):
    '''Upload single orig image'''

    user = models.ForeignKey(User,
                             related_name="orig_images",
                             on_delete=models.CASCADE
                             )
    orig_image = models.ImageField(upload_to="images",
                                   validators=[validate_image_file_extension])

    def __str__(self):
        return f"{self.get_filename}"

    @property
    def get_imageurl(self):
        return self.orig_image.url

    @property
    def get_imagepath(self):
        return self.orig_image.path

    @property
    def get_filename(self):
        return os.path.split(self.orig_image.path)[-1]

    def get_absolute_url(self):
        return reverse_lazy("croppedimages:crop_orig_image_url", kwargs={'pk': self.id})


class CroppedImageFile(models.Model):
    '''Upload cropped images: Cropper.js'''

    user = models.ForeignKey(User,
                             related_name="cropped_images",
                             on_delete=models.CASCADE
                             )
    orig_image = models.ForeignKey("croppedimages.OrigImageFile",
                                   related_name="cropped_images",
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True
                                   )
    image = models.ImageField(upload_to="cropped_images")

    def __str__(self) -> str:
        return f"{self.get_filename}"

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
        return reverse_lazy("croppedimages:orig_images_list_url")
