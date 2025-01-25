from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='blog_image', blank=True, null=True)  # Allows blog image uploads
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'

    

# # Profile Model
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_image', blank=True, null=True)

#     def __str__(self):
#         return f'Profile of {self.user.username}'
    

# class CustomUser(AbstractUser):
#     phone = models.CharField(max_length=15, blank=True)
#     address = models.TextField(blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)



