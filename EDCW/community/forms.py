from django import forms


class PostForm(forms.Form):
	Category_List=(
		(1,'赛事公告'),
		(2,'技术讨论'),
		(3,'各路水贴'),
		)
	title = forms.CharField(max_length=100,error_messages={'required':u'标题不能为空'})
	outline = forms.CharField(max_length=100,required=False)
	body = forms.CharField(max_length=100,error_messages={'required':u'正文不能为空'})
	category=forms.IntegerField(
		widget=forms.Select(choices=Category_List),
		error_messages={'required':u'类型不能为空'}
		)

class CommentForm(forms.Form):
	comment= forms.CharField(max_length=1000)

