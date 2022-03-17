from django.core.exceptions import ValidationError

from .models import Alumni
from base.models import Document

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

class AlumniCreationForm(forms.ModelForm):
    
    def clean_user(self):
        email = self.cleaned_data['email']
        user, _ = User.objects.get_or_create(email=email)
        alumni = Group.objects.get(name='alumni')
        user.username = email[:len(email)-12]
        user.set_password('anteater')
        user.groups.add(alumni)
        user.save()
        return user

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Alumni
        fields = ['name', 'usn', 'phone', 'email', 'personal_email', 'branch', 'year_joined', 'year_passed', 'user']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the name"}),
            'usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'branch': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the branch"}),
            'year_joined': forms.SelectDateWidget(attrs={"class": "form-select"}),
            'year_passed': forms.SelectDateWidget(attrs={"class": "form-select"}),
        }


class AlumniUploadForm(forms.ModelForm):
    def validate_file(file):
        if not file.name.endswith('.csv'):
            raise ValidationError("Only csv file format supported!")
        return file

    file = forms.FileField(validators=[validate_file], widget=forms.FileInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Document
        fields = ["name", "file"]
