from django import forms
from .models import Order


from django import forms

class OrderCreateForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email address')
    # Add any additional fields you need for your form

    # If you want to include the order notes field, you can uncomment the following line
    # order_notes = forms.CharField(label='Order notes', widget=forms.Textarea, required=False)