from django.contrib import admin

from .models import Post #se refiere al objeto Post del archivo models
# Register your models here.
# para administrar los modelos

admin.site.register(Post)

