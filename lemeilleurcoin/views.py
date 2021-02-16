from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import Advert


class AdvertsList(LoginRequiredMixin, ListView):
    """
    Display list of adverts
    """

    model = Advert
