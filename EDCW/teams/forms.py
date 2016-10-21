from django import forms
from .models import Team, pre_time_choice

class AppForm(forms.Form):
    reason = forms.CharField(max_length=300, required=False)

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20)
    intro = forms.CharField(max_length=50)
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)


class GroupForm(forms.Form):
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)



class FirstTimeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FirstTimeForm, self).__init__(*args, **kwargs)
        s = pre_time_choice
        for team in Team.objects.filter(pre_time__gte = 1):
            print(team)
            print(s)
            s = [choice for choice in s if choice[0] != team.pre_time]
        self.fields['choice'].choices = s

    choice = forms.ChoiceField(choices=())
