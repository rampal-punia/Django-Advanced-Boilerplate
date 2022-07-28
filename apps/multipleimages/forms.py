from django import forms
from django.core.validators import validate_image_file_extension
from .models import MultipleImageFile


class MultipleImagesUploadForm(forms.ModelForm):
    image = forms.FileField(
        validators=[validate_image_file_extension],
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = MultipleImageFile
        fields = ['image']
