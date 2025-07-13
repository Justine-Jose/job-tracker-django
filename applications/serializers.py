from rest_framework import serializers
from .models import JobApplications

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplications
        fields = '__all__'
        read_only_fields = ['user']