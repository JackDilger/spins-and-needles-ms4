from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    """ A view for the blog page """

    posts = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ A view for each blog post """

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
