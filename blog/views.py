from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import Posts
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.query import QuerySet
# Create your views here.


class PostListView(ListView):
    model = Posts
    template_name = 'post_list.html'

class PostListView(ListView):
    model = Posts
    template_name = 'post_list.html'
    def get_queryset(self): 
        queryset = Posts.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset=queryset.filter(Q(title__contains=q) | Q(info__contains=q))
        return queryset
    
class PostDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'
    count_hit = True

    def get(self, request, *args, **kwargs):
        print("PostDetailView is called!")
        return super().get(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'info','image']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostCreateView(CreateView):
    model=Posts
    template_name='post_new.html'
    fields = ['title', 'info','image','time']
    success_url = reverse_lazy('post_list')




