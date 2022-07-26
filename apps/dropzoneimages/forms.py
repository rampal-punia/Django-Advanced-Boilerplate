from django import forms
from .models import ImagesUpload


class DzImagesUploadForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ImagesUpload
        fields = ['image']
