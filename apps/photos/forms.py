from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject"}))
    message = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Message"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
