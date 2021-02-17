from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Advert


class AdvertsList(LoginRequiredMixin, ListView):
    """
    Display list of adverts
    """

    model = Advert


class CreateAdvert(LoginRequiredMixin, CreateView):
    """
    Create a new advert
    """

    model = Advert
    fields = ["title", "description", "price", "picture"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("advert", kwargs={"pk": self.object.pk})


class AdvertDetail(LoginRequiredMixin, DetailView):
    """
    Display an advert in details
    """

    model = Advert
