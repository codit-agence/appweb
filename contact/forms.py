from django import forms
from .models import Contact, ContactInscription


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message','title','tel','ville']


class ContactInscriptionForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message','tel','ville']