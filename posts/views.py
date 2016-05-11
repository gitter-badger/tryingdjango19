from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>create</h1>")
def post_detail(request, id): # retrieve
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : "detail",
        "instance" : instance
    }
    return render(request, "post_detail.html", context)
def post_list(request): # list items
    #if request.user.is_authenticated:
        #context 1
    #else
        #context 2
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title" : "List"
    }
    # return HttpResponse("<h1>list</h1>")
    return render(request, "index.html", context)
def post_update(request):
    return HttpResponse("<h1>update</h1>")
def post_delete(request):
    return HttpResponse("<h1>delete</h1>")