from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='news-home'),
    path('searchresult/', views.SearchResultList.as_view(), name='search_urls'),
    path('contact/', views.ContactPageView.as_view(), name='news-contact'),
    path('mahhalliy/', views.LocalNewsView.as_view(), name='news-mahhalliy'),
    path('xorijiy/', views.ForeignNewsView.as_view(), name='news-xorijiy'),
    path('texnologiya/', views.TechnologyNewsView.as_view(), name='news-texnologiya'),
    path('sport/', views.SportNewsView.as_view(), name='news-sport'),
    path('create/', views.NewsCreateView.as_view(), name='news-create'),
    path('update/<slug:slug>/', views.NewsUpdateView.as_view(), name='news-update'),
    path('delete/<slug:slug>/', views.NewsDeleteView.as_view(), name='news-delete'),
    path('<slug:slug>/', views.news_detail, name='news-detail'),
    
]