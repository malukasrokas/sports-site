
from django import forms
from .models import Post, ForumPost, Comment, Team, Player, Match

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'team',)

class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ('title', 'post',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'homeArena',)

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'height', 'bDay', 'team')
        
class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('homeTeam', 'homeTeamScore', 'awayTeamScore', 'awayTeam', 'date',)
