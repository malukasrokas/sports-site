from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

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
    news = models.ForeignKey(Post, null=True)
    forumPost = models.ForeignKey(ForumPost, null=True)
    text = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author

class Team(models.Model):
    name = models.CharField(max_length=50)
    homeArena = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    bDay = models.DateTimeField()
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.name

class Stats(models.Model):
    player = models.ForeignKey(Player)
    score = models.IntegerField()

    def __str__(self):
        return self.player

class Match(models.Model):
    homeTeam = models.ForeignKey(Team, related_name='homeTeam')
    awayTeam = models.ForeignKey(Team, related_name='awayTeam')
    date = models.DateTimeField()

    def __str__(self):
        return self.homeTeam, self.awayTeam
