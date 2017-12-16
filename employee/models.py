from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class This_Job(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=500)
    short_text = models.TextField()
    time = models.CharField(max_length=50)
    skill = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
