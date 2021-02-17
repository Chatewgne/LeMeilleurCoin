from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CustomUserCreationForm


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CustomUserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to login on success
            return HttpResponseRedirect("/accounts/login")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/customuser_form.html", {"form": form})
