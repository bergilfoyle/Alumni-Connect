from django.urls import path, re_path

from .views import AlumniListView, AlumniCreateView, AlumniUploadView, AlumniDeleteView, AlumniPostView, AlumniSearchView
from base.views import IPView

from base.decorators import switch_view

urlpatterns = [
    path('', AlumniListView.as_view(), name = 'list_alumni'),
    path('new', switch_view(AlumniCreateView.as_view(), IPView.as_view(), IPView.as_view()), name = 'new_alumni'),
    path('upload', switch_view(AlumniUploadView.as_view(), IPView.as_view(), IPView.as_view()), name = 'upload_alumni'),
    path("delete/<int:pk>/", AlumniDeleteView.as_view(), name="delete_alumni"),
    path('posts', AlumniPostView.as_view(), name='list_alumni_post'),
    path('search', AlumniSearchView.as_view(), name='search_alumni'),
]