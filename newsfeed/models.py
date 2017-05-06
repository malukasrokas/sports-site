from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    team = models.ForeignKey('Team', related_name="related_posts", null=True, blank=True)

    class Meta:
        ordering = ['-created_date',]

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    post = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Chat(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=140)
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    newsPost = models.ForeignKey(Post, blank=True, null=True, related_name="news_comments")
    forumPost = models.ForeignKey(ForumPost, blank=True, null=True, related_name="forum_comments")
    text = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Team(models.Model):
    name = models.CharField(max_length=50)
    homeArena = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField(validators=[MinValueValidator(0)])
    bDay = models.DateTimeField()
    team = models.ForeignKey(Team, related_name="players", blank=True, null=True)

    def __str__(self):
        return self.name

class Stats(models.Model):
    player = models.ForeignKey(Player)
    score = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.player

class Match(models.Model):
    homeTeam = models.ForeignKey(Team, related_name='homeTeam')
    homeTeamScore = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    awayTeam = models.ForeignKey(Team, related_name='awayTeam')
    awayTeamScore = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    date = models.DateTimeField()
