from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import include, path, re_path

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('applicant-form/', views.ApplicantForm.as_view(), name="applicant-form"),
    path('Post-a-job/', views.Jobform.as_view(), name="Post-a-job"),
    url(r'^search/$', views.Search.as_view(), name="search"),
    url(r'^add-applicant/', views.AddApplicant.as_view()),
    url(r'^add-jobs/', views.AddJob.as_view()),
]
