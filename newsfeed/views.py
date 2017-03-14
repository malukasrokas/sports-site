from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'newsfeed/post_list.html', {'posts': posts})

def post_in_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newsfeed/post_in_detail.html', {'post': post})
