from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Advert(models.Model):
    """
    Model for adverts
    """

    # A short title for the advert
    title = models.CharField(max_length=150, verbose_name="Titre")
    # Description of the advertised product
    description = models.TextField(verbose_name="Description")
    # Price of the advertised product
    price = models.IntegerField(
        validators=[MinValueValidator(0, "Entrer une valeur positive.")],
        verbose_name="Prix (€)",
    )
    # User who posted the advert
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # Picture of the advertised product
    picture = models.ImageField(
        verbose_name="Photo", default="templates/no-image.png"
    )
