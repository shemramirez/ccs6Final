from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

'''
posts = [
    {
        'author':'George',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018',
    },
    {
        'author':'Jane',
        'title':'Blog post 2',
        'content':'second post content',
        'date_posted':'August 28, 2018',
    }
]
'''

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def performance(request):
    return render(request, 'blog/performance.html')