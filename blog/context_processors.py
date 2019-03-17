from .models import Post

def all(request):
    latest_posts = Post.objects.latest_posts()
    popular_posts = Post.objects.popular_posts()
    featured_posts = Post.objects.featured_posts()

    return {
        'latest_posts': latest_posts,
        'popular_posts' : popular_posts,
        'featured_posts' : featured_posts
    }