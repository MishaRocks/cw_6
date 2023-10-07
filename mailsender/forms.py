from django import forms
from django.forms import modelformset_factory

from mailsender.models import Message, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'

    message_title = forms.CharField(max_length=200, required=True, label='Тема сообщения')
    message_content = forms.CharField(widget=forms.Textarea, required=True, label='Текст сообщения')

    is_active = forms.BooleanField(required=False, initial=True, label='Активно')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['message_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['message_content'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})


MessageFormSet = modelformset_factory(Message, form=MessageForm, extra=1)
