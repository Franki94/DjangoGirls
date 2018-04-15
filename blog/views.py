from django.shortcuts import render, get_object_or_404

from .models import Post #Para importar el modelo Post

from django.utils import timezone
# Create your views here.
#Esta primera parte, indica la direccion del html
# def post_list(request):
#         return render(request, 'blog/post_list.html', {})

#asi enviamos un queryset al html
def post_list(request):
        posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, postId):
        post = get_object_or_404(Post, id = postId)
        return render(request, 'blog/post_detail.html', {'post' : post})