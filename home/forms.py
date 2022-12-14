from django import forms
from .models import Post, Comment


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Type your comment here'})
        }
        labels = {
            "body": ""
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control ', 'rows': 3, 'placeholder': 'Type your reply here'})
        }
        labels = {
            "body": ""
        }


class PostSearchForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'special', 'placeholder': 'Search here'}))
