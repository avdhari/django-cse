from django.shortcuts import render
from .models import Post


def home_view(request):
    post_list = Post.objects.all().order_by('-published_date')
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/home.html', context)


def detail_view(request):
    return render(request, 'blog/post_detail.html')
