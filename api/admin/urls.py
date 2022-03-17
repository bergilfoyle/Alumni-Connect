from django.urls import path, re_path
from base.views import IPView
from .views import UploadView, ReportView, HelpView
from base.decorators import switch_view

urlpatterns = [
    path('upload', switch_view(UploadView.as_view(), IPView.as_view(), IPView.as_view()), name='upload_admin'),
    path('reports', switch_view(ReportView.as_view(), IPView.as_view(), IPView.as_view()), name='reports'),
    path('help', switch_view(HelpView.as_view(), IPView.as_view(), IPView.as_view()), name='help')
]