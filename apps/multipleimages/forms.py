from dataclasses import field
from django import forms
from .models import MultipleImageFile


class MultipleImagesUploadForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta: 
        model = MultipleImageFile
        fields = ['image']
