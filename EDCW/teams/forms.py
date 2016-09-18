from django import forms

class AppForm(forms.Form):
    reason = forms.CharField(max_length=300, required=False)

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20)
    intro = forms.CharField(max_length=50)

