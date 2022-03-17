from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView
import time
from django.forms import ValidationError
from .forms import UploadForm
from .analysis import generate
from django.urls import reverse

class AdminHomeView(TemplateView):
    template_name = 'admin/home.html'

class HelpView(TemplateView):
    template_name = 'admin/help.html'

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'admin/upload.html'

    def form_valid(self, form):
        #status = generate(self.request.FILES["file"])
        #if not status:
        #    raise ValidationError('Invalid File Structure!')
        time.sleep(5)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reports')

class ReportView(TemplateView):
    template_name = 'admin/reports.html'