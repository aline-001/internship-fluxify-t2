from django.shortcuts import render, get_object_or_404
from .models import Blogpost


def post_list(request):
    posts = Blogpost.objects.all()
    return render(request, 'posts/post_list.html', {'posts:posts'})


def post_details(request, id):
    post = get_object_or_404(Blogpost, id=id)
    return render(request, 'post_details.html', {'post:post'})
