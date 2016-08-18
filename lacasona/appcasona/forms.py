from django import forms
from .models import Message
from crispy_forms.helper import FormHelper

class MessageListFormHelper(FormHelper):
    model = Message
    form_tag = False