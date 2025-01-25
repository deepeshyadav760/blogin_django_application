from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'Myblogapp/blog_list.html', {'blogs': blogs})

def blog_details(request, id):
    blog = get_object_or_404(Blog, pk=id)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'Myblogapp/blog_details.html', {'blog': blog, 'comments': comments})


@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)

        if title and content and category:
            blog.title = title
            blog.content = content
            blog.category = category
            blog.save()
            return redirect('Myblogapp:blog_details', id=blog.id)

    categories = Category.objects.all()
    return render(request, 'Myblogapp/update_blog.html', {'blog': blog, 'categories': categories})

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('Myblogapp:blog_list')  # Add namespace
    return render(request, 'Myblogapp/delete_blog.html', {'blog': blog})


@login_required
def add_comment(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(blog=blog, user=request.user, content=content)
            return redirect('Myblogapp:blog_details', id=blog.id)
    return redirect('Myblogapp:blog_details', id=blog.id)



# Add this function
def add_default_categories():
   categories = [
       'Technology',
       'Travel',
       'Food',
       'Lifestyle',
       'Health',
       'Business'
   ]
   
   for cat_name in categories:
       Category.objects.get_or_create(name=cat_name)

# Update create_blog view
@login_required
def create_blog(request):
   # Add default categories if none exist
   if Category.objects.count() == 0:
       add_default_categories()
       
   if request.method == 'POST':
       title = request.POST.get('title')
       content = request.POST.get('content')
       category_id = request.POST.get('category')
       category = get_object_or_404(Category, id=category_id)
       

       if title and content and category:
           Blog.objects.create(
               title=title,
               content=content, 
               category=category,
               author=request.user
           )
           return redirect('Myblogapp:blog_list')

   categories = Category.objects.all()
   return render(request, 'Myblogapp/create_blog.html', {'categories': categories})


def user_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('Myblogapp:blog_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'Myblogapp/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('Myblogapp:blog_list')
    return render(request, 'Myblogapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('Myblogapp:user_login')