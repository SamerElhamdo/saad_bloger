from django.shortcuts import render

from django.views import generic
from .models import Post, Book, Telawa



class Home(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'post_list'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context.update({
            'book_list': Book.objects.order_by('-created_on'),
            'telawa_list': Telawa.objects.all(),
        })
        return context

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')
        
class Posts(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'post_list'
    paginate_by = 9
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created_on')




class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'