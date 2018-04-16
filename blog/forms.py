from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta(object):
        model = Post #El modelo que usa para el formulario
        fields = ('title', 'text',) #Los campos que deseamos