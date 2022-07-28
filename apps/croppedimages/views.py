import os
import cv2

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

from .models import CroppedImageFile, OrigImageFile


class OrigImageUploadView(LoginRequiredMixin, CreateView):
    model = OrigImageFile
    fields = ["orig_image"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrigImageDetailView(LoginRequiredMixin, DetailView):
    model = OrigImageFile
    context_object_name = "orig_image"


class CroppedImageListView(LoginRequiredMixin, ListView):
    '''Displays Orig images with their corresponding cropped images'''

    model = OrigImageFile
    context_object_name = 'images_qs'
    template_name = "croppedimages/croppedimagefile_list.html"
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        qs = OrigImageFile.objects.filter(user=user)
        return qs


class CroppedImageDetailView(LoginRequiredMixin, DetailView):
    model = CroppedImageFile
    context_object_name = "cropped_image"


class CroppedImageSaveView(View):
    '''Handled by the ajax call from the single image detail view.'''

    def post(self, *args, **kwargs):
        context = {}
        img_id = int(self.request.POST.get("imageId"))

        img_x = self.request.POST.get('x')
        img_y = self.request.POST.get('y')
        img_w = self.request.POST.get('w')
        img_h = self.request.POST.get('h')
        crop = self.request.POST.get("crop")
        if crop:
            if not (img_x is None or img_y is None or img_w is None or img_h is None):
                img_x, img_y, img_w, img_h = int(float(img_x)), int(float(
                    img_y)), int(float(img_w)), int(float(img_h))

                orig_img = OrigImageFile.objects.get(id=img_id)
                img = cv2.imread(orig_img.get_imagepath)
                try:
                    cropped_img = img[img_y:img_y+img_h, img_x:img_x+img_w]

                    ret, buf = cv2.imencode(".jpg", cropped_img)

                    cropped_img_qs = self.create_croppedimgmodel_from_crop(
                        orig_img, buf)
                    message = f"Image file: {orig_img} is successfully uploaded."
                    cropped_img_url = reverse_lazy("croppedimages:cropped_image_detail_url", args=[
                        cropped_img_qs.id])
                    context["success"] = "success"
                    context["img_url"] = cropped_img_qs.get_imageurl
                    context["cropped_img_id"] = cropped_img_qs.id
                    context["cropped_img_url"] = cropped_img_url
                    context["message"] = message
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
    success_url = reverse_lazy("croppedimages:cropped_images_list_url")
