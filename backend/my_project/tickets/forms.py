from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'client',
            'status',
            'priority',
            'category',
            'channel',
            'agent',
            'title',
            'description',
        ]