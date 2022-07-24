import os
import cv2

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.files.base import ContentFile
# from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import ImageFile, ImageGroup, BatchImageFile, CroppedImageFile
from . import helper


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        images_qs = ImageFile.objects.filter(user=user)
        context["image_qs"] = images_qs
        return context


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


class CroppedImageUploadView(LoginRequiredMixin, CreateView):
    model = CroppedImageFile
    fields = ["image"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CroppedImageListView(LoginRequiredMixin, ListView):
    '''Displays Orig images with their corresponding cropped images'''

    model = ImageFile
    context_object_name = 'images_qs'
    template_name = "imageuploader/croppedimagefile_list.html"
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        qs = ImageFile.objects.filter(user=user)
        return qs


class CroppedImageDetailView(LoginRequiredMixin, DetailView):
    model = CroppedImageFile
    context_object_name = "cropped_image"


class CroppedImageSaveView(View):
    '''Handled by the ajax call from the single image detail view.'''

    def post(self, *args, **kwargs):
        context = {}
        img_id = int(self.request.POST.get("imageId"))
        print(img_id)

        img_x = self.request.POST.get('x')
        img_y = self.request.POST.get('y')
        img_w = self.request.POST.get('w')
        img_h = self.request.POST.get('h')
        crop = self.request.POST.get("crop")
        print(img_x, img_y, img_h, img_w)
        if crop:
            if not (img_x is None or img_y is None or img_w is None or img_h is None):
                img_x, img_y, img_w, img_h = int(float(img_x)), int(float(
                    img_y)), int(float(img_w)), int(float(img_h))

                orig_img = ImageFile.objects.get(id=img_id)
                print("orig_img", orig_img)
                img = cv2.imread(orig_img.get_imagepath)
                print("img", img)
                try:
                    cropped_img = img[img_y:img_y+img_h, img_x:img_x+img_w]

                    ret, buf = cv2.imencode(".jpg", cropped_img)

                    cropped_img_qs = self.create_croppedimgmodel_from_crop(
                        orig_img, buf)
                    messages.success(
                        self.request, f"Image file: {orig_img} is successfully uploaded.")
                    cropped_img_url = reverse_lazy("imageuploader:cropped_image_detail_url", args=[
                        cropped_img_qs.id])
                    print("img_url", cropped_img_qs.get_imageurl)
                    print("cropped_img_url", cropped_img_url)
                    context["success"] = "success"
                    context["img_url"] = cropped_img_qs.get_imageurl
                    context["cropped_img_id"] = cropped_img_qs.id
                    context["cropped_img_url"] = cropped_img_url
                    return JsonResponse(context)
                except Exception as e:
                    print(e)
                    context["exception"] = "failed"
                    return JsonResponse(context)

    def create_croppedimgmodel_from_crop(self, orig_img, buf):
        content = ContentFile(buf.tobytes())
        crop_img_qs = CroppedImageFile.objects.create(
            user=self.request.user,
            orig_image=orig_img,
        )
        crop_img_qs.image.save(
            f"{os.path.splitext(orig_img.get_filename)[0]}.jpg", content)
        return crop_img_qs


class CroppedImageDeleteView(LoginRequiredMixin, DeleteView):
    model = CroppedImageFile
    success_url = reverse_lazy("imageuploader:cropped_images_list_url")
