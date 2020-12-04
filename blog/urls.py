from django.urls import path
from .views import BlogListView, BlogViewDetail

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/' , BlogViewDetail.as_view(), name='post_detail'),
]