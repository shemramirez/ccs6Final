from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(),name='post-detail'),
    path('about/', views.about,name='blog-about'),
    path('performance/', views.performance,name='blog-performance'),
    path('grades/', views.grades,name='blog-grades'),
    path('chatroom/', views.chat, name='blog-chat'),

]
