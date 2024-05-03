from django.shortcuts import render
from django.db.models.functions import Length
from .models import Post, Comment

def home(request):
    posts = Post.objects.all()
    author_stats = []

    for post in posts:
        comments = Comment.objects.filter(post=post)
        comments_count = comments.count()
        comments_long = list(filter(lambda x: len(x.text) >= 5, comments))
        # comments_long = Comment.objects.annotate(text_len = Length("text")).filter(post=post, text_len__gte=5)
        # long_comments_count = comments_long.count()
        # long_comments_count = sum(1 for comment in comments if len(comment.text) >= 5)

        author_stats.append({
            'post': post,
            'comments_count': comments_count,
            'long_comments_count': len(comments_long)
        })

    return render(request, 'home.html', {'author_stats': author_stats})
