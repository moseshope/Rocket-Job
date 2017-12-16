from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class ProfileEmp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.BooleanField(null=False, default=False)
    company = models.CharField(max_length=500, null=True)
    website = models.URLField(max_length=200, null=True)
    address1 = models.CharField(max_length=500, null=True)
    address2 = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=200, default='Chittagong')
    country = models.CharField(max_length=200, default='Bangladesh')
    about = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class ProfileFree(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    freelancer = models.BooleanField(null=False, default=False)
    portfolio = models.URLField(max_length=200, null=True)
    address1 = models.CharField(max_length=500, null=True)
    address2 = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=200, default='Chittagong')
    country = models.CharField(max_length=200, default='Bangladesh')
    about = models.TextField(null=True)

    def __str__(self):
        return self.user.username


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    superuser = models.BooleanField(null=False, default=False)
#    freelancer = models.BooleanField(null=False, default=False)
#    employee = models.BooleanField(null=False, default=False)

#    def __str__(self):
#        return self.user.username

#used to make a profile automatically for a new user
#@receiver(post_save, sender=User)
#def create_or_update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()
