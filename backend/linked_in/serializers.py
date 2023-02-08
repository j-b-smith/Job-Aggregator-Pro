from rest_framework import serializers
from .models import Job

# Blueprint for converting model to json key value pairs

class JobSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Job
        fields = (
            'id', 
            'title', 
            'company_name', 
            'job_type', 
            'remote_status', 
            'salary_start', 
            'salary_end',
            'date_listed',
            'created_at'
            )