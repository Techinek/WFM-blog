from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryPosts.as_view(), name='category'),
    path('tag/<str:slug>/', TagPosts.as_view(), name='tag'),
    path('post/<str:slug>/', SinglePost.as_view(), name='post')
]