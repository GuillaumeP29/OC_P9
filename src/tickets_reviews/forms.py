from django import forms
from django.forms.fields import BooleanField
from django.forms.widgets import HiddenInput
from . import models


RATINGS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
    ]


class TicketForm(forms.ModelForm):
    edit_ticket = BooleanField(widget=HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=RATINGS)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteTicketForm(forms.ModelForm):
    delete_ticket = BooleanField(widget=HiddenInput, initial=True)


# class HiddenTicketForm(forms.Form):
#     ticket_id = forms.IntegerField(widget=HiddenInput)
