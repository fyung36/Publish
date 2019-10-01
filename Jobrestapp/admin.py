from django.contrib import admin
from .models import Applicant, Post_Job, Applications
# Register your models here.

admin.site.register(Applicant)
admin.site.register(Post_Job)
admin.site.register(Applications)