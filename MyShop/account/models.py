from django.db import models
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Orders
from django.contrib.auth.models import User , AbstractBaseUser, PermissionsMixin, BaseUserManager






class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'profile')
    full_name = models.CharField(max_length = 100, blank= True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()




