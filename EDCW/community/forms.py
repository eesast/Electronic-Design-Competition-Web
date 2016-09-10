from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=100)
    outline = forms.CharField(max_length=100,required=False)
    body = forms.CharField(max_length=100)
	
	
class CommentForm(forms.Form)
    