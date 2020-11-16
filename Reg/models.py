from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=20,blank=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    pro,crt= Profile.objects.get_or_create(user=instance)
    if not crt:
        instance.profile.save()


class Post(models.Model):

    text = models.CharField(max_length=256, blank=False, default='')
    V_user = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE, null=True)
