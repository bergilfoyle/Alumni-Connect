from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student
from comments.models import Comment
from django.contrib.auth.models import User

from .forms import StudentCreationForm, StudentUploadForm

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView

from base.file_handlers import handle_student_csv
from .parsers import parse_query

def response(request):
    return HttpResponse('Hello')

class StudentHomeView(TemplateView):
    template_name = 'student/home.html'

class StudentListView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    ordering = ['user']

class StudentSearchView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    arg = {}

    def get(self, request):
        self.__class__.arg = parse_query(request.GET['query'])
        return super().get(self, request)

    ordering = ['user']

    def get_queryset(self):
        return Student.objects.filter(**self.__class__.arg)

class StudentCommentView(ListView):
    model = Comment
    template_name = 'comments/list.html'
    context_object_name = 'posts'
    ordering = ['posted_by']

    def get_queryset(self):
        return Comment.objects.filter(posted_by=self.request.user)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreationForm
    template_name = 'student/new.html'

    def get_success_url(self):
        return reverse('list_student')

class StudentUploadView(FormView):
    form_class = StudentUploadForm
    template_name = 'student/upload.html'

    def form_valid(self, form):
        handle_student_csv(self.request.FILES["file"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('list_student')

class StudentDeleteView(DeleteView):
    model = User

    def get_success_url(self):
        return reverse('list_student')