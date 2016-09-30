from django import forms
from .models import Team

class AppForm(forms.Form):
    reason = forms.CharField(max_length=300, required=False)

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20)
    intro = forms.CharField(max_length=50)
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)


class GroupForm(forms.Form):
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)
