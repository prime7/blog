from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
	news = News.objects.all()

	context = {
		'all_news' : news,
	}
	return render(request,"news/news.html",context)