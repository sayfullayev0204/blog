from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProfileCreateView, ProfileListView, ProfileUpdateView,ProfileDetailView

urlpatterns = [
    path('<int:pk>/edit/', ProfileUpdateView.as_view(), name="profile_edit"),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('new/', ProfileCreateView.as_view(), name='profile_new'),
    path('', ProfileListView.as_view(), name='profile_list'),
    
]



