from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name", "type": "text", "name": "name", "class": "form-control rounded-0"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject","type": "text", "name": "subject", "class": "form-control rounded-0"}))
    message = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Message", "type": "text", "name": "message", "class": "form-control rounded-0"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "type": "email", "name": "email", "class": "form-control rounded-0"}))

