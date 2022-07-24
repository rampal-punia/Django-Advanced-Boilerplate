from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from singleimages import models


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        images_qs = models.ImageFile.objects.filter(user=user)
        context["image_qs"] = images_qs
        return context
