from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post
from .forms import PostCreateForm
from django.db.models import Q,F


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if request.GET:
            posts = Post.objects.active()
            query = request.GET["q"]
            if query:
                posts = posts.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct() # author, author_id, content, date_posted, id, title
                return render(request, self.template_name, {'posts': posts})
        return super().get(request, *args, **kwargs)
    
    # def get_queryset(self):
    #     print("query1")
    #     if self.request.GET:
    #         print("query2")
    #         print(self.request.GET["search"])
    #         posts = Post.objects.active()
    #         query = self.request.GET["search"]
    #         if query:
    #             print("query3")
    #             posts = posts.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
    #             return render(self.request, self.template_name, {'posts': posts})
    #     return Post.objects.all().order_by('-date_posted')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            query = self.request.GET["q"]
            print(query)
        posts = Post.objects.active()
        latest_posts = Post.objects.latest_posts()
        popular_posts = Post.objects.popular_posts()
        context.update({
            'latest_posts': latest_posts,
            'posts' : posts ,
            'popular_posts' : popular_posts
        })
        return context
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.active()
        latest_posts = Post.objects.latest_posts()
        popular_posts = Post.objects.popular_posts()
        context.update({
            'latest_posts': latest_posts,
            'posts' : posts ,
            'popular_posts' : popular_posts
        })
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post.views = F('views') + 1  # Using an F expression to avoid race conditions
        post.save()
        posts = Post.objects.active()
        latest_posts = Post.objects.latest_posts()
        popular_posts = Post.objects.popular_posts()
        context.update({
            'latest_posts': latest_posts,
            'posts' : posts ,
            'popular_posts' : popular_posts
        })
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
