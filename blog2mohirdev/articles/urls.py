from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleUpdate, ArticleDelete, ArticleCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article-edit'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article-delete'),
    path('article/new/', ArticleCreate.as_view(), name='article-create'),

]
