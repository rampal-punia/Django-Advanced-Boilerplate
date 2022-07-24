from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import ImageFile


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


class SingleImageDeleteView(LoginRequiredMixin, DeleteView):
    model = ImageFile
    context_object_name = "image"
    success_url = reverse_lazy("singleimages:single_image_list_url")
