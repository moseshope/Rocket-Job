from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from employee.models import This_Job

# Create your models here.


class Bid(models.Model):
    job = models.ForeignKey(This_Job, default=1, on_delete=models.CASCADE, related_name='bids')
    bid_poster = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    bid_text = models.TextField()
    bid_time = models.CharField(max_length=50)
    bid_budget = models.CharField(max_length=50)
    bid_posted_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.job.title
