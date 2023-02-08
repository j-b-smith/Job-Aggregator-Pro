from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20)
    remote_status = models.CharField(max_length=8)
    salary_start = models.IntegerField()
    salary_end = models.IntegerField()
    date_listed = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
