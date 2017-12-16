from django.db import models
from django.utils import timezone

# Create your models here.


class Job(models.Model):
    website = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    short_text = models.TextField()
    #job_type = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    skill = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title # + ' --Posted On ' + self.website
