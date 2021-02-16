from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    """
    Extend user model with a phone number
    """

    # Regex for number validation
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+99999999999'. Up to 15 digits allowed.",
    )
    # Phone number
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
    )
    # TODO profile picture


class Advert(models.Model):
    """
    Model for adverts
    """

    # A short title for the advert
    title = models.CharField(max_length=150)
    # Description of the advertised product
    description = models.TextField()
    # Price of the advertised product
    price = models.IntegerField()
    # User who posted the advert
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # TODO image

    def __str__(self):
        return self.title