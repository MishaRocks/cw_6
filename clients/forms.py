from django import forms

from clients.models import Client
from users.forms import StyleFormMixin


class ClientsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'name', 'surname', 'comment', 'letters')
