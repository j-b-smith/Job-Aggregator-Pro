from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_logo_url = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20)
    remote_status = models.CharField(max_length=8)
    salary_start = models.IntegerField()
    salary_end = models.IntegerField()
    date_listed = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.title
    