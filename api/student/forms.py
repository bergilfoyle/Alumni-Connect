from django.core.exceptions import ValidationError

from .models import Student
from base.models import Document

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms


class StudentCreationForm(forms.ModelForm):

    def clean_user(self):
        email = self.cleaned_data['email']
        user, _ = User.objects.get_or_create(email=email)
        students = Group.objects.get(name='students')
        user.username = email[:len(email)-12]
        user.set_password('anteater')
        user.groups.add(students)
        user.save()
        return user

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Student
        fields = ['name', 'usn', 'sap_id', 'phone', 'email',
                  'personal_email', 'branch', 'year_joined', 'user']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the name"}),
            'usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'sap_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the SAP ID"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'branch': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the branch"}),
            'year_joined': forms.SelectDateWidget(attrs={"class": "form-select"}),
        }


class StudentUploadForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.csv'):
            raise ValidationError(
                "Only csv file format supported!", code='invalid')
        return file

    class Meta:
        model = Document
        fields = (
            "name",
            "file",
        )
        widgets = {'file': forms.FileInput(attrs={"class": "form-control"})}
