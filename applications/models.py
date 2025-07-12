from django.db import models

# Create your models here.
class JobApplications(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    applied_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[('Applied', 'Applied'), ('Interviewing', 'Interviewing'), ('Offered', 'Offered'), ('Rejected', 'Rejected')],
        default='Applied'
    )
    note = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.company_name} - {self.position}"