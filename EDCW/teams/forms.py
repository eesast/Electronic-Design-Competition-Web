from django import forms
from .models import Team, fuhuo_time_choice

class AppForm(forms.Form):
    reason = forms.CharField(max_length=300, required=False)

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20)
    intro = forms.CharField(max_length=50)
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)


class GroupForm(forms.Form):
    group = forms.ChoiceField(choices=Team.GROUP_CHOICES)



class FuhuoTimeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FuhuoTimeForm, self).__init__(*args, **kwargs)
        s = fuhuo_time_choice
        for team in Team.objects.filter(fuhuo_time__gte = 1):
            s = [choice for choice in s if choice[0] != team.fuhuo_time]
        self.fields['choice'].choices = s

    choice = forms.ChoiceField(choices=())
    other = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'placeholder': u'若都不合适，请输入合适时间'}))
