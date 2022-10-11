from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from profiles.models import UserProfile


# Credit djangocentral(see readme credits section)
def posts(request):
    """ A view for the blog page """

    posts = Post.objects.filter(status=1).order_by('-event_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    """
    A view for each blog post
    """

    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            comment_form = CommentForm(initial={
                'email': profile.user.email,
                'name': profile.user.username
                })
        else:
            comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
