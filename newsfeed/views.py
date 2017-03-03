from django.shortcuts import render

def post_list(request):
    return render(request, 'newsfeed/post_list.html', {})
