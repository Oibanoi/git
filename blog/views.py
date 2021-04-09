from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from blog.models import Post,Comment 
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.
class PostListView(ListView):
    queryset=Post.objects.all().order_by("date")
    template_name = 'blog/blog.html'
    context_object_name='Posts'
    paginate_by=2
def post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = CommentForm()
    if request.method=="POST":
        form= CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request,"blog/post.html",{"post":post,"form":form})
class BlogCreateView(CreateView):
    model=Post
    template_name='blog/post_new.html'
    fields=['title','author','body']