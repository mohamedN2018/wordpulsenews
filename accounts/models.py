from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    links = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save.connect(save_user_profile, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    instance.profile.delete()
post_save.connect(delete_user_profile, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save()        
post_save.connect(update_user_profile, sender=User)
def get_user_profile(user):
    try:
        return user.profile
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_id(user_id):
    try:
        return Profile.objects.get(user_id=user_id)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_username(username):
    try:
        return Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_email(email):
    try:
        return Profile.objects.get(user__email=email)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_phone(phone):
    try:
        return Profile.objects.get(phone=phone)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_address(address):
    try:
        return Profile.objects.get(address=address)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_date_of_birth(date_of_birth):
    try:
        return Profile.objects.get(date_of_birth=date_of_birth)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_created_at(created_at):
    try:
        return Profile.objects.get(created_at=created_at)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_updated_at(updated_at):
    try:
        return Profile.objects.get(updated_at=updated_at)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_images(images):
    try:
        return Profile.objects.get(images=images)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_links(links):

    try:
        return Profile.objects.get(links=links)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_media(media):
    try:
        return Profile.objects.get(media=media)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_active(is_active):
    try:
        return Profile.objects.get(is_active=is_active)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_verified(is_verified):
    try:
        return Profile.objects.get(is_verified=is_verified)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_admin(is_admin):
    try:
        return Profile.objects.get(is_admin=is_admin)
    except Profile.DoesNotExist:
        return None
    