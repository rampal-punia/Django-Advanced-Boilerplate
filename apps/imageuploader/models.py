import os

from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from . import helper

User = settings.AUTH_USER_MODEL


class ImageFile(models.Model):
    '''Upload single image'''
    user = models.ForeignKey(User,
                             related_name="images",
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

    def get_absolute_url(self):
        return reverse_lazy("imageuploader:single_image_detail_url", kwargs={"pk": self.pk})


class ImageGroup(models.Model):
    '''Image group for the batch images.'''
    user = models.ForeignKey(User,
                             related_name="image_groups",
                             on_delete=models.CASCADE
                             )

    title = models.CharField(max_length=101)

    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("imageuploader:image_group_detail_url", kwargs={"pk": self.pk})


class BatchImageFile(models.Model):
    '''Upload multiple images: Dropzone.'''

    file = models.ImageField(upload_to="batch_images")

    img_grp = models.ForeignKey("imageuploader.ImageGroup",
                                name="Image Group",
                                related_name="images",
                                on_delete=models.CASCADE
                                )

    @property
    def get_imageurl(self):
        return self.file.url

    @property
    def get_imagepath(self):
        return self.file.path

    @property
    def get_filename(self):
        return os.path.split(self.file.path)[-1]

    # def get_absolute_url(self):
    #     return reverse("imageuploader:model_detail_url", kwargs={"pk": self.pk})


class CroppedImageFile(models.Model):
    '''Upload cropped images: Cropper.js'''

    user = models.ForeignKey(User,
                             related_name="cropped_images",
                             on_delete=models.CASCADE
                             )
    orig_image = models.ForeignKey("imageuploader.ImageFile",
                                   related_name="cropped_images",
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True
                                   )
    image = models.ImageField(upload_to="cropped_images")

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
        return reverse("imageuploader:model_detail_url", kwargs={"pk": self.pk})
