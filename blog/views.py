from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Comment
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin 

# Create your views here.
# def home_view(request):
#     return HttpResponse("<h1>Home Page</h1>")

# def about_view(request):
#     return HttpResponse("<h1>About Page</h1>")

# def contact_view(request):
#     return HttpResponse("<h1>Contact Page</h1>")

# def home_view(request):
#     return render(request,"home_page.html")

# Function Based View

# def about_view(request):
#     return render(request,"about_page.html")

# def contact_view(request):
#     return render(request,"contact_page.html")

# def blog_detail_view(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     # {title:"",body:""}
#     return render(request,"blog_detail_page.html",{"post":post})


# def blog_list_view(request):
#     posts = Post.objects.all() # [{title:"",body:""}, {}, {}]
#     return render(request, "home_page.html", {"post_list": posts }) # {"post_list" : [{title:"",body:""}, {}, {}]}
#                                             #    |>>this is context

# Class Based View     
#                                         
# READ (CRUD)
class BlogAboutListView(ListView):
    model=Post
    template_name="about_page.html"

class BlogContactListView(ListView):
    model=Post
    template_name="contact_page.html"

class BlogListView(ListView): #[{},{}]
    model=Post
    template_name="home_page.html"

class BlogDetailView(LoginRequiredMixin,DetailView): # {}
    model=Post
    template_name="blog_detail_page.html"
    form_class=CommentForm
    
# CREATE (CRUD)
class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="blog_create_page.html"
    form_class=PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentCreateView(LoginRequiredMixin,CreateView):
    model=Comment
    template_name="comment_create_page.html"
    form_class=CommentForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        post_id = self.kwargs.get('pk')   #2
        form.instance.post = get_object_or_404(Post, pk=post_id)
        return super().form_valid(form)
    
# UPDATE (CRUD)
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostForm

    def test_func(self): # This returns true when author is same loged in user or as return false
        obj = self.get_object()
        return obj.author == self.request.user

# DELETE (CRUD)
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "post_delete.html"
    # success_url = reverse_lazy("home_page")  # safe side operation  

    def get_success_url(self):
        return reverse("home_page")  
    # 
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

        # if "modi" in self.request.user.username:
        #     return True
        # else:
        #     return False