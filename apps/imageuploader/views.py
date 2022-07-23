from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ImageFile


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class SingleImageUploadView(LoginRequiredMixin, CreateView):
    model = ImageFile
    fields = ["image"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SingleImageListView(LoginRequiredMixin, ListView):
    model = ImageFile
    context_object_name = 'single_images'
    paginate_by = 50

    def get_queryset(self):
        user = self.request.user
        qs = ImageFile.objects.filter(user=user)
        return qs


class SingleImageDetailView(LoginRequiredMixin, DetailView):
    model = ImageFile
    context_object_name = "image"
