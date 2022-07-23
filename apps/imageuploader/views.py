from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ImageFile


class ImageUploadView(LoginRequiredMixin, CreateView):
    model = ImageFile
    fields = ["image"]
