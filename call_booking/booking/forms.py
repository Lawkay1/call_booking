from django import forms
from .models import Book

class CallBookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'email', 'phone', 'date', 'time', 'hours']
