from django.db import models
from django.contrib.auth.models import User
from employee.models import This_Job
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    post_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='post_user')
    comment_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='comment_user')
    job = models.ForeignKey(This_Job, default=1, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_user.username
