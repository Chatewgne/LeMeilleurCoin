from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
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
