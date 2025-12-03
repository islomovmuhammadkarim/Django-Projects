from django.shortcuts import get_object_or_404, render,redirect
from django.template import context
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import News, Category,Comment
from .forms import ContactForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .custom_permissions import OnlySuperUser,OnlyAuthorOrSuperUser,OnlyStaffUser
from django.db.models import Q
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

class HomePageView(ListView):
    model = News
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['news']=News.published.all().order_by('-published_time')[:5]
        context['categories']=Category.objects.all()
        context['mahhalliy_news']=News.published.all().filter(category__name='Mahalliy').order_by('-published_time')[0:5]
        context['xorijiy_news']=News.published.all().filter(category__name='Xorij').order_by('-published_time')[0:5]
        context['texnologiya_news']=News.published.all().filter(category__name='Texnologiya').order_by('-published_time')[0:5]
        context['sport_news']=News.published.all().filter(category__name='Sport').order_by('-published_time')[0:5]
        return context


def news_detail(request,slug):
    news=get_object_or_404(News,slug=slug,status=News.Status.PUBLISHED)

    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits += 1


    related_news=News.published.all().filter(category=news.category).exclude(id=news.id).order_by('-published_time')[:3]
    
    comments=news.comments.filter(active=True)
    comment_count=comments.count()
    new_comment=None
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.news=news
            new_comment.author=request.user
            new_comment.user=request.user
            new_comment.save()
            return redirect('news-detail',slug=news.slug)
    else:
        comment_form=CommentForm()
    
    context={
        "news":news,
        "related_news":related_news,
        "comments":comments,
        "new_comment":new_comment,
        "comment_form":comment_form,
        "total_hits":hits,
        "comment_count":comment_count,
    }
    return render(request,'news/detail.html',context)


class NewsUpdateView(OnlyAuthorOrSuperUser,LoginRequiredMixin,UpdateView):
    model = News
    template_name = 'news/update_news.html'
    fields = ['title','body','image','category','status']
    success_url = reverse_lazy('news-home')

class NewsCreateView(OnlySuperUser,CreateView):
    model = News
    template_name = 'news/create_news.html'
    fields = ['title','body','image','category','status']
    success_url = reverse_lazy('news-home')

class NewsDeleteView(OnlyAuthorOrSuperUser,DeleteView):
    model = News
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('news-home')


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahhalliy_news.html'
    context_object_name = 'mahhalliy_news'

    def get_queryset(self):
        news=self.model.published.all().filter(category__name='Mahalliy')
        return news
class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorijiy_news.html'
    context_object_name = 'xorijiy_news'
    
    def get_queryset(self):
        news=self.model.published.all().filter(category__name='Xorij')
        return news 
class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/texnologiya_news.html'
    context_object_name = 'texnologiya_news'
    
    def get_queryset(self):
        news=self.model.published.all().filter(category__name='Texnologiya')
        return news   
class SportNewsView(ListView):
    model = News
    template_name = 'news/sport_news.html'
    context_object_name = 'sport_news'
     
    def get_queryset(self):
        news=self.model.published.all().filter(category__name='Sport')
        return news
class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request,*args,**kwargs):
        form=ContactForm()
        context={
            "form":form
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news-contact")
        context={
            "form":form
        }
        return render(request,self.template_name,context)        
        
    
class SearchResultList(ListView):
    model=News
    template_name='news/search_result.html'
    context_object_name='search_result'
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        return self.model.published.all().filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
            )