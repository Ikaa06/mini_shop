from django import forms
from home.models import Reservation, Applications


class ReservationForm(forms.ModelForm):
    """ Создание заказа """

    class Meta:
        model = Reservation
        fields = ("name", "email", "phone")


class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ("name", "phone")