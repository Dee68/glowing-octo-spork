from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from product.models import Customer
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created==False:
        instance.userprofile.save()
    

@receiver(post_save, sender=User)
def create_customer(sender, instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if created==False:
        instance.customer.save()

@receiver(user_logged_in, sender=User)
def instatiate_user_profile(sender, user, request, **kwargs):
    if user==request.user:
        UserProfile.objects.create(user=user)

@receiver(user_logged_in, sender=User)
def instatiate_customer(sender, user, request, **kwargs):
    if user==request.user:
        Customer.objects.create(user=user)

    