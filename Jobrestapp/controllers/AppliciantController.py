from rest_framework.response import Response
from ..models import Applicant, Post_Job, Applications
from ..forms import ApplicantForm, Postjobform
from ..serializers import Applicantserializers, Postserializers


class ApplicantController():

    def getAllApplicants(self):
        applicants = Applicant.objects.all()
        return applicants

    def SearchForApplicants(self, searchBasedOn, searchInputValue):
        filters = {
            searchBasedOn: searchInputValue
        }
        searchedApplicants = Applicant.objects.filter(**filters)
        return searchedApplicants

    def AddApplicant(self, applicantData):
        formData = ApplicantForm(applicantData)
        if formData.is_valid():
            applicant = Applicant(
                FirstName=applicantData['FirstName'],
                LastName=applicantData['LastName'],
                Email=applicantData['Email'],
                Age=applicantData['Age'],
                Job_Position=applicantData['Job_Position']
            )
            applicant.save()
            applicantFiltered = Applicant.objects.filter(pk=applicant.pk)
            serializer = Applicantserializers(applicantFiltered, many=True)
            return Response(serializer.data)
        return Response("form is not valid")

class Postjobcontroller():

    def getAllJobs(self):
        jobs = Post_Job.objects.all()
        return jobs

    def Addjobs(self, jobData):
        formData = Postjobform(jobData)
        if formData.is_valid():
            Postedjob = Post_Job(
                Job_title=jobData['Job_title'],
                Job_Description=jobData['Job_Description'],
                Company=jobData['Company'],
                Location=jobData['Location'],
                Job_type=jobData['Job_type'],

            )
            Postedjob.save()
            PostjobFiltered = Post_Job.objects.filter(pk=Postedjob.pk)
            serializer = Postserializers(PostjobFiltered, many=True)
            return Response(serializer.data)
        return Response("form is not valid")

class Applicationcontroller():

    def getApplication(self):
        Apply = Applications.objects.all()
        return Apply
