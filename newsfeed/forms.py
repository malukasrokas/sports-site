from django import forms

from .models import Post, ForumPost, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ('title', 'post',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
