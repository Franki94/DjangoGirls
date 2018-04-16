"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from blog import views

#path(route, view, kwargs=None, name=None)
urlpatterns = [
    # re_path(r'^', views.post_list, name='post_list'),#Cuando queremos usar expresiones regulares
    path('', views.post_list, name='post_list'),#en la url vacia, inserta el post_list del view
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/<int:postId>/', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:postId>/edit/', views.post_edit, name='post_edit'),

    path('drafts/', views.post_draft_list, name = 'post_draft_list'),
    path('post/<int:postId>/publish/', views.post_publish, name='post_publish'),
]
