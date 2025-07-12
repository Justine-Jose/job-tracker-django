from rest_framework import serializers
from .models import JobApplications

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplications
        fields = '__all__'