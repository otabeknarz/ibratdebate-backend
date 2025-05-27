import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from ibratdebate.base_model import BaseModel


def get_random_id():
    return uuid.uuid4().hex


class Region(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class District(BaseModel):
    name = models.CharField(max_length=255)
    telegram_group_link = models.URLField(max_length=255, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name="districts")

    def __str__(self):
        return self.name


class User(AbstractUser):
    class EnglishLevelChoices(models.TextChoices):
        B1_B2 = "B1-B2", "B1-B2"
        C1_C2 = "C1-C2", "C1-C2"

    class AgeChoices(models.TextChoices):
        LESS_THAN_16 = "<16", "<16"
        BETWEEN_16_18 = "16-18", "16-18"
        BETWEEN_19_24 = "19-24", "19-24"
        MORE_THAN_24 = ">24", ">24"

    id = models.CharField(primary_key=True, max_length=40, default=get_random_id)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name="users")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name="users")
    age = models.CharField(choices=AgeChoices.choices, max_length=10, null=True, blank=True)

    english_level = models.CharField(max_length=255, null=True, blank=True, choices=EnglishLevelChoices.choices)

    language_code = models.CharField(max_length=10, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password if self.password else self.id)

        super(User, self).save(*args, **kwargs)
