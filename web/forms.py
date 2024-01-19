from django import forms

from .models import Contact,Enquiryform


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiryform  
        exclude = ("timestamp", "service") 