"""lemeilleurcoin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AdvertsList, CreateAdvert, AdvertDetail

urlpatterns = [
    # Admin page :
    path("admin/", admin.site.urls),
    # Login page :
    path(
        "login/",
        auth_views.LoginView.as_view(),
        name="login",
    ),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # List all adverts :
    path("adverts/", AdvertsList.as_view(), name="adverts"),
    # Create an advert :
    path("adverts/new", CreateAdvert.as_view(), name="new-advert"),
    # See an advert in detail :
    path("adverts/<int:pk>", AdvertDetail.as_view(), name="advert"),
]
