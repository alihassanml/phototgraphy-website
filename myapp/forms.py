from django import forms
from .models import image

class imageupload(forms.ModelForm):
    class Meta:
        model = image
        fields = '__all__'
        image = {'image': ' '}