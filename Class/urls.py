from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>', views.article.as_view(), name='article'),
    path('post', views.post.as_view(), name='post'),
    path('edit/<int:pk>', views.edit.as_view(), name='edit'),
    path('purge/<int:pk>', views.purge.as_view(), name='purge'),
    path('tag', views.tag.as_view(), name='tag'),
    path('category/<str:slug>', views.category, name='category'),
    path('categories', views.categories.as_view(), name='categories'),
    path('like/<int:pk>', views.like, name='like'),
    path('user/<int:pk>', views.user, name='user'),
]
