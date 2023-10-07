from django import forms

from logs.models import Logs
from mailsender.forms import StyleFormMixin


class MailingLogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Logs
        fields = '__all__'