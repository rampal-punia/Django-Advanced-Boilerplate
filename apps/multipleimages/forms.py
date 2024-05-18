from django import forms
from django.core.validators import validate_image_file_extension
from .models import MultipleImageFile


class MultipleImagesUploadForm(forms.ModelForm):
    image = forms.FileField(
        validators=[validate_image_file_extension],
        widget=forms.ClearableFileInput()
    )

    class Meta:
        model = MultipleImageFile
        fields = ['image']


class CustomClearableFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        attrs = {'multiple': True} if attrs is None else {**attrs, 'multiple': True}
        super().__init__(attrs)
