from django import forms
from .models import CodeShare, CodeAsk, ShareComment, ShareRe

class ShareNew(forms.ModelForm):
    class Meta:
        model = CodeShare
        fields = ['title','image','body','codes','subject','university','score','writer']

class AskNew(forms.ModelForm):
    class Meta:
        model = CodeAsk
        fields = ['title','image','body','codes','subject','writer']

class ShareCommentForm(forms.ModelForm):
    class Meta:
        model = ShareComment
        fields=['sharecontents']

class ShareReForm(forms.ModelForm):
    class Meta:
        model = ShareRe
        fields=['resharecontents']