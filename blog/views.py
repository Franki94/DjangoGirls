from django.shortcuts import render, get_object_or_404

from .models import Post #Para importar el modelo Post

from django.utils import timezone #para implementar la hora

from django.shortcuts import redirect

from .forms import PostForm

from django.contrib.auth.decorators import login_required #para añadir el decorador y restringir el acceso

# Create your views here.
#Esta primera parte, indica la direccion del html
# def post_list(request):
#         return render(request, 'blog/post_list.html', {})

#asi enviamos un queryset al html
def post_list(request):
        posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')#el - indica que sera ordenado de forma descendiente
        return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, postId):
        post = get_object_or_404(Post, id = postId)
        return render(request, 'blog/post_detail.html', {'post' : post})
@login_required
def post_new(request):
        if request.method == 'POST':
                form = PostForm(request.POST)
                if form.is_valid():
                        Post = form.save(commit=False)
                        Post.author = request.user
                        Post.save()
                        return redirect('post_detail', postId = Post.id)
        else:
                form = PostForm()
        return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, postId):
        post = get_object_or_404(Post, id = postId)#id se refiere al id del modelo
        if request.method == 'POST':
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                        post = form.save(commit=False)
                        post = request.user
                        post.save()
                        return redirect('post_detail', postId = post.id)
        else:
                form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})        

@login_required
def post_draft_list(request):
        posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
        return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def post_publish(request, postId):
        post = get_object_or_404(Post, id = postId)
        post.publish()
        return redirect('post_detail', postId= post.id)
        
@login_required
def post_remove(request, postId):
        post = get_object_or_404(Post, id = postId)
        post.delete()
        return redirect('post_list')