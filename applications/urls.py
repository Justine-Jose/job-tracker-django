from django.urls import path
from .views import JobApplicationDetials, JobApplicationListCreate
from . import views


urlpatterns = [
    path('',views.dashboard, name = 'dashboard'),
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetials.as_view(), name='job-detail'),
    path('jobs/add/',views.add_job_page, name = 'add-job-page'),
    path('jobs/list/',views.list_job_page, name = 'list-job-page')
    
]