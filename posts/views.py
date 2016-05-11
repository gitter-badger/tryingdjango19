from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    
    # creating the instance of PostForm class
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print (form.cleaned_data.get("title"))
        instance.save()
    #if request.method == "POST":
        #print (request.POST.get("title"))
        #print (request.POST.get("content"))
    context = {
        "form": form, 
    }
    return render(request, "post_form.html", context)
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