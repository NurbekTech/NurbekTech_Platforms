from django.shortcuts import render
from .models import Post


# Create your views here.
def blog(request):
    data = {"posts": Post.objects.all()}
    return render(request, "blog/blog.html", context=data)
