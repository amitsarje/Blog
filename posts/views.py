from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def posts_detail(request , id=None):
    #queryset  = Post.objects.all()
    instance = get_object_or_404(Post , id=id)
    context = {
        "title":instance.title,
        "instance":instance
        
    }
    return render(request , "post_detail.html" , context) 

@login_required(login_url='/login/')
def posts_list(request):
    queryset  = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "obj_list":queryset,
        "title":"list" ,
        "page_obj":page_obj,
        "page_number":page_number  
    }
    return render(request , "index.html" , context) 



@login_required
def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request , "New post added")
        return redirect(instance.get_abs_url())
    context={
        "form":form,
    }
    return render(request , "p_form.html" , context) 

def login1(request):
    if request.method=='POST':
        username = request.POST.get('Username')
        password =  request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            messages.error(request , "User not found")
            return redirect('/login/')
    else:
        return render(request , 'login.html')

@login_required
def logout1(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method=='POST':
        username = request.POST['Username']
        password =request.POST['password']
        fname =request.POST['fname']
        lname = request.POST['lname']
        if  User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")   
            return redirect("/signup/")
        else:
            user=User.objects.create_user(username=username , password=password  , first_name=fname , last_name=lname)
            user.save()
            messages.success(request , "User registered successfully")
            return redirect("/login/")
    else:
        return render(request,'signup.html')


@login_required
def posts_update(request , id=None):
    instance = get_object_or_404(Post , id=id)
    form = PostForm(request.POST or None , instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request , "post updated")
        return redirect(instance.get_abs_url())
    context = {
        "title":instance.title,
        "instance":instance,
        "form":form
        
    }
    return render(request , "p_form.html" , context)

@login_required
def posts_delete(request , id=None):
     instance = get_object_or_404(Post , id=id)
     instance.delete()
     return redirect('/')


