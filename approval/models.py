# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):

    USER_TYPES = (
        ('d', 'doctor'),
        ('p', 'patient'),
        ('m','pharmacist'),
    )

    user = models.CharField(max_length=150)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='p')
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

class Prescription(models.Model):
    user = models.ForeignKey(UserProfile)
    content = models.TextField()

class RequestQ(models.Model):
    STATUS_TYPES = (('p', 'Pending'),('a', 'Approved'))
    requested_by = models.IntegerField(null=False)
    requested_to = models.IntegerField(null=False)
    status = models.CharField(max_length=1,default='p',choices=STATUS_TYPES)


