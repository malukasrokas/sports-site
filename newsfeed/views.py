from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post, ForumPost
from .forms import PostForm, ForumPostForm, CommentForm

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'newsfeed/post_list.html', {'posts': posts})

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
    return render(request, 'forum/forum_list.html', {'forumPosts': forumPosts})

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

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_in_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'newsfeed/add_comment_to_post.html', {'form': form})
