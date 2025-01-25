"""
URL configuration for Myblogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Myblogapp'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='blog_create'),
    path('<int:id>/', views.blog_details, name='blog_details'),
    path('<int:id>/update/', views.update_blog, name='blog_update'),
    path('<int:id>/delete/', views.delete_blog, name='blog_delete'),
    path('<int:id>/comment/', views.add_comment, name='add_comment'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)