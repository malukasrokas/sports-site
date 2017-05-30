from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Post, ForumPost, Comment, Team, Player, Match
from .forms import PostForm, ForumPostForm, CommentForm, TeamForm, PlayerForm, MatchForm

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    teams = Team.objects.all()
    paginated_posts = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_page = paginated_posts.page(page)
    except PageNotAnInteger:
        post_page = paginated_posts.page(1)
    except EmptyPage:
        post_page = paginated_posts.page(paginated_posts.num_pages)
    return render(request, 'newsfeed/post_list.html', {
        'posts': posts,
        'post_page': post_page,
        'teams': teams
    })

def post_list_filtered(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team_posts = Post.objects.filter(team=team)
    paginated_posts = Paginator(team_posts, 2)
    page = request.GET.get('page')
    try:
        post_page = paginated_posts.page(page)
    except PageNotAnInteger:
        post_page = paginated_posts.page(1)
    except EmptyPage:
        post_page = paginated_posts.page(paginated_posts.num_pages)
    return render(request, 'newsfeed/post_list_filtered.html', {
        'team': team,
        'team_posts': team_posts,
        'post_page': post_page
    })

def post_in_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newsfeed/post_in_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_in_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newsfeed/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_in_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'newsfeed/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def forum_list(request):
    forumPosts = ForumPost.objects.order_by('-timeStamp')
    paginated_posts = Paginator(forumPosts, 2)
    page = request.GET.get('page')
    try:
        post_page = paginated_posts.page(page)
    except PageNotAnInteger:
        post_page = paginated_posts.page(1)
    except EmptyPage:
        post_page = paginated_posts.page(paginated_posts.num_pages)

    return render(request, 'forum/forum_list.html', {
        'forumPosts': forumPosts,
        'post_page': post_page
    })

def forumpost_detail(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    return render(request, 'forum/forumpost_detail.html', {'forumpost' : forumpost})

def new_forumpost(request):
    if request.method == "POST":
        form = ForumPostForm(request.POST)
        if form.is_valid():
            forumpost = form.save(commit=False)
            forumpost.author = request.user
            forumpost.published_date = timezone.now()
            forumpost.save()
            return redirect('forumpost_detail', pk=forumpost.pk)
    else:
        form = ForumPostForm()
    return render(request, 'forum/edit_forumpost.html', {'form': form})

def edit_forumpost(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=forumpost)
        if form.is_valid():
            forumpost = form.save(commit=False)
            forumpost.author = request.user
            forumpost.published_date = timezone.now()
            forumpost.save()
            return redirect('forumpost_detail', pk=forumpost.pk)
    else:
        form = ForumPostForm(instance=forumpost)
    return render(request, 'forum/edit_forumpost.html', {'form': form})

def remove_forumpost(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    forumpost.delete()
    return redirect('forum_list')

@login_required
def add_comment_to_post(request, pk):
    newsPost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.newsPost = newsPost
            comment.save()
            return redirect('post_in_detail', pk=newsPost.pk)
    else:
        form = CommentForm()
    return render(request, 'newsfeed/add_comment_to_post.html', {'form': form})

@login_required
def remove_news_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    newsPost_pk = comment.newsPost.pk
    comment.delete()
    return redirect('post_in_detail', pk=newsPost_pk)

@login_required
def add_comment_to_forumpost(request, pk):
    forumPost = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.forumPost = forumPost
            comment.save()
            return redirect('forumpost_detail', pk=forumPost.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_forumpost.html', {'form': form})

@login_required
def remove_forum_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    forumpost_pk = comment.forumPost.pk
    comment.delete()
    return redirect('forumpost_detail', pk=forumpost_pk)

def teams(request):
    teams = Team.objects.order_by('-name')
    return render(request, 'teams/all_teams.html', {'teams': teams})

@login_required
def add_team(request):
    form = TeamForm()
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            return render(request, 'teams/all_teams.html', {'form': form})

    return render(request, 'teams/add_team.html', {'form': form})

def team_summary(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team_players = Player.objects.filter(team=pk)
    return render(request, 'teams/team_summary.html', {
        'team': team,
        'team_players':team_players
    })

@login_required
def add_player(request):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('player_summary', pk=player.pk)

    return render(request, 'teams/add_player.html', {'form': form})

@login_required
def edit_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('player_summary', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'teams/add_player.html', {'form': form})

def player_summary(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'teams/player_summary.html', {'player': player})

def matches(request):
    matches = Match.objects.order_by('-date')
    return render(request, 'matches/matches_list.html', {'matches': matches})

@login_required
def add_match(request):
    form = MatchForm()
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            return render(request, 'matches/matches_list.html', {'form': form})

    return render(request, 'matches/add_match.html', {'form': form})

def match_summary(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'matches/match_summary.html', {'match': match})

@login_required
def edit_match_summary(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            return redirect('match_summary', pk=match.pk)
    else:
        form = MatchForm(instance=match)
    return render(request, 'matches/add_match.html', {'form': form})
