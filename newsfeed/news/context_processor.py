from .models import News,Category

def latest_news(request):
    latest_news=News.published.all().order_by('-published_time')[:10]
    popular_news=News.published.all().order_by('-published_time')[:5]
    categories=Category.objects.all()
    context={
        'latest_news': latest_news,
        'popular_news': popular_news,
        'categories': categories
        }
    return context