from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplications
from .serializers import JobApplicationSerializer
from django.utils.decorators import method_decorator    
from django.views.decorators.csrf import csrf_exempt

class JobApplicationListCreate(APIView):
    def get(self,request):
        jobs = JobApplications.objects.all()
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobApplicationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class JobApplicationDetials(APIView):
    def get_object(self,pk):
        try:
            return JobApplications.objects.get(pk=pk)
        except JobApplications.DoesNotExist:
            return None
        
    def get(self, request, pk):
        job = self.get_object(pk)
        if job is None:
            return Response({"error": "Not Found"}, status=404)
        serializer = JobApplicationSerializer(job)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        if job is None:
            return Response({"error": "Not Found"}, status=404)
        serializer = JobApplicationSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("PUT request failed validation:", serializer.errors)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        job = self.get_object(pk)
        if job is None:
            return Response({"error": "Not Found"}, status=404)
        job.delete()
        return Response(status=204)
    
def add_job_page(request):
    return render(request,'jobs/add_job_api.html')

def list_job_page(request):
    return render(request,'jobs/list_jobs_api.html')

def dashboard(request):
    return render(request,'jobs/dashboard.html')

