from .models import Applicant,Post_Job
from django import forms

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['FirstName', 'LastName', 'Email', 'Age', 'Job_Position']

class Postjobform(forms.ModelForm):
    JOBTYPE = (
        ('Full Time', 'FullTime'), ('Part Time', 'PartTime'), ('Freelance', 'FreeLance'), ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
    )

    Jobtype = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=JOBTYPE)


    class Meta:
        model = Post_Job
        fields = ['Job_title','Company','Job_Description','Location','Jobtype']
        # widgets = {'job_type': forms.RadioInput}