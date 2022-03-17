from django.forms import ValidationError
from django.http import HttpResponse
from django.urls import reverse

from .models import Alumni, Placements
from posts.models import Post
from django.contrib.auth.models import User

from .forms import AlumniCreationForm, AlumniUploadForm

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView

from .handlers import handle_alumni_csv
from .parsers import parse_query

def response(request):
    return HttpResponse('Hello')

class AlumniHomeView(TemplateView):
    template_name = 'alumni/home.html'

class AlumniListView(ListView):
    model = Alumni
    template_name = 'alumni/list.html'
    context_object_name = 'alumni'
    ordering = ['user']

class AlumniSearchView(ListView):
    model = Alumni
    template_name = 'alumni/list.html'
    context_object_name = 'alumni'
    arg = {}

    def get(self, request):
        self.__class__.arg = parse_query(request.GET['query'])
        return super().get(self, request)

    ordering = ['user']

    def get_queryset(self):
        return Alumni.objects.filter(**self.__class__.arg)

class AlumniPostView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    ordering = ['author']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.alumnus_details)

class AlumniCreateView(CreateView):
    model = Alumni
    form_class = AlumniCreationForm
    template_name = 'alumni/new.html'

    def get_success_url(self):
        return reverse('list_alumni')

class AlumniUploadView(FormView):
    form_class = AlumniUploadForm
    template_name = 'alumni/upload.html'

    def form_valid(self, form):
        status = handle_alumni_csv(self.request.FILES["file"])
        if not status:
            raise ValidationError('Invalid File Structure!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('list_alumni')

class AlumniDeleteView(DeleteView):
    model = User

    def get_success_url(self):
        return reverse('list_alumni')