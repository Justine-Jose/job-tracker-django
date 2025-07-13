from django.urls import path
from .views import JobApplicationDetials, JobApplicationListCreate
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('',views.dashboard, name = 'dashboard'),
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetials.as_view(), name='job-detail'),
    path('jobs/add/',views.add_job_page, name = 'add-job-page'),
    path('jobs/list/',views.list_job_page, name = 'list-job-page'),
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html',authentication_form = LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]