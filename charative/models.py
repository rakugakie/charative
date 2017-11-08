from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Modifiable(models.Model):
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class TimeCreatable(models.Model):
    created = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Modifiable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    short_bio = models.TextField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Chara(Modifiable, TimeCreatable):
    owner = models.ManyToManyField(User)
    name = models.CharField(unique=False, max_length=50)
    avatar = models.ImageField(upload_to='chara_images',blank=True)
