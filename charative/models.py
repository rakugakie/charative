from django.db import models


class Modifiable(models.Model):
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class TimeCreatable(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)


class Chara(Modifiable, TimeCreatable):
    name = models.CharField(unique =False, max_length=50)
    picture = models.ImageField(upload_to='chara_images',blank=True)
