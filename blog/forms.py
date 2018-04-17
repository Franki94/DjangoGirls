from django import forms

from .models import Post, Comment

#aca situamos los componentes que tendran los formularios 

class PostForm(forms.ModelForm):

    class Meta(object):
        model = Post #El modelo que usa para el formulario
        fields = ('title', 'text',) #Los campos que deseamos

class CommentForm(forms.ModelForm):

    class Meta(object):
        model = Comment
        fields = ('author', 'text',)