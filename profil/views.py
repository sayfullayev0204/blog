from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import Profile
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.query import QuerySet

# Create your views here.


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'

    def get(self, request, *args, **kwargs):
        print("PostDetailView is called!")
        return super().get(request, *args, **kwargs)
    
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['name', 'lastname','age','t_yil','img']
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile_list')

class ProfileCreateView(CreateView):
    model=Profile
    template_name='profile/profile_new.html'
    fields = ['name', 'lastname','age','t_yil','img']
    success_url = reverse_lazy('profile_list')
