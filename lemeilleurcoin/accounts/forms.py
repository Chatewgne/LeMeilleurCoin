from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Extend user creation form with phone number
    """

    class Meta:
        model = CustomUser
        fields = ("username", "phone_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        """
        Change labels in UI form
        """
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["phone_number"].label = "Numéro de téléphone"
        self.fields["password1"].label = "Mot de passe"
        self.fields["password2"].label = "Confirmation du mot de passe"


class CustomUserChangeForm(UserChangeForm):
    """
    Extend user change form with phone number
    """

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number")
