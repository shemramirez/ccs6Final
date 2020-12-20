from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
'''from django.contrib.auth.forms import Listview'''




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

'''
class SearchView(ListView):
    model = Products
    template_name = 'grades.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Products.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result
'''
def get_blog_query(query = None):
    queryset = []
    queries = query.split(" ") 
    for q in queries:
        post = Post.objects.filter(
            Q(title__icontains=q) |
            Q(author__icontains=1)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))

    