from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from .utils import get_read_time



class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(approved=True)
    
    def latest_posts(self, *args, **kwargs):
        return super(PostManager, self).filter(approved=True).order_by('-date_posted')[:3]
    
    def popular_posts(self, *args, **kwargs):
        return super(PostManager, self).filter(approved=True).order_by('-views')[:3]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    read_time =  models.IntegerField(default=0)


    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


def create_slug(instance,new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    
    if instance.content:
        html_string = instance.content
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var
    

pre_save.connect(pre_save_post_receiver,sender=Post)