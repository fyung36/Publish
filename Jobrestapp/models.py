from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
FullTime = 'Fulltime'
PartTime = 'Partimes'
FreeLance = 'Freelance'
Internship = 'Internship'
Temporary = 'Temporary'


class Applicant(models.Model):
    """ Applicant profile in our app """

    def __str__(self):
        return"{} {}".format(self.FirstName, self.LastName)

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250, unique=True)
    Age = models.IntegerField(default=0)
    Job_Position = models.CharField(max_length=250)



class Post_Job(models.Model):
    Job_title = models.CharField(max_length=250)
    Company = models.CharField(max_length=250, default="")
    Location = models.CharField(max_length=250, default="")
    Job_Description = models.TextField()
    JOBTYPE = (
        ('Full Time', FullTime), ('Part Time', PartTime), ('Freelance', FreeLance), ('Internship', Internship),
        ('Temporary', Temporary),
    )
    Job_type = models.CharField(max_length=65, choices=JOBTYPE, null=False, default="")
    applicants = models.ManyToManyField(Applicant, through='Applications')
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return "{}".format(self.Job_title)

    def get_types(self):
        return self.Job_type

    def get_absolute_url(self):
         return reverse("applicant-form", kwargs={"id": self.id})

class Applications(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    postjob = models.ForeignKey(Post_Job, on_delete=models.CASCADE)
