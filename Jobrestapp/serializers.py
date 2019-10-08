from .models import Applicant, Post_Job
from rest_framework import serializers

class Applicantserializers(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ('FirstName','LastName', 'Email', 'Age', 'Job_Position')

class Postserializers(serializers.ModelSerializer):

    Jobtype = serializers.ChoiceField(choices=Post_Job.JOBTYPE)

    class Meta:
        model = Post_Job
        fields = ('Job_title','Company','Job_Description','Location','Jobtype')
