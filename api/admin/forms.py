from django.core.exceptions import ValidationError

from base.models import Document

from django.contrib.auth.models import User
from django import forms

class UploadForm(forms.ModelForm):
    def validate_file(file):
        if not file.name.endswith('.xlsx'):
            raise ValidationError("Only csv file format supported!")
        return file

    file = forms.FileField(validators=[validate_file], widget=forms.FileInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Document
        fields = ["name", "file"]