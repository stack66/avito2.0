from django import forms

class RenewFlatForm(forms.Form):
    region = forms.ChoiceField()
