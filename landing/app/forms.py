from django.forms import ModelForm, EmailField, DateTimeField, DateTimeInput, Select
from .models import ContactPrice


class FormContactPrice(ModelForm):
    email = EmailField(max_length=255, help_text='Bitte eine email eingeben...')

    class Meta:
        model = ContactPrice
        fields = ('name', 'email', 'message', 'phone')

