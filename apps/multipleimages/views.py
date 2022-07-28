from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MultipleImageFile
from .forms import MultipleImagesUploadForm


class MultipleImagesUploadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = MultipleImagesUploadForm()
        context = {
            'form': form
        }
        return render(request, 'multipleimages/multipleimagefile_form.html', context)

    def post(self, *args, **kwargs):
        form = MultipleImagesUploadForm(
            self.request.POST, self.request.FILES)
        uploaded_images = self.request.FILES.getlist('image')
        if len(uploaded_images) > 1:
            multiple_files = True
            # Do something, if required, or simply delete this part.
        else:
            multiple_files = False
            # Do something else

        if form.is_valid:
            for index, file in enumerate(uploaded_images):
                self.request.FILES['image'] = file
                # or anything else you want to display/ or delete this part
                print(f"working on file {index + 1}:{file}")

                user = self.request.user
                img = MultipleImageFile(image=file, user=user)
                img.save()
        return HttpResponseRedirect(reverse_lazy("multipleimages:multiple_image_list_url"))


class MultipleImageListView(LoginRequiredMixin, ListView):
    model = MultipleImageFile
    context_object_name = 'multi_images'
    paginate_by = 50
    ordering = ['-id']

    def get_queryset(self):
        user = self.request.user
        qs = MultipleImageFile.objects.filter(user=user)
        return qs


class MultipleImageDeleteView(LoginRequiredMixin, DeleteView):
    model = MultipleImageFile
    context_object_name = "image"
    success_url = reverse_lazy("multipleimages:multiple_image_list_url")
