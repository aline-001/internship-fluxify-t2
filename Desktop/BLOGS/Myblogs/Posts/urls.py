from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_details, name='post_details'),
]
