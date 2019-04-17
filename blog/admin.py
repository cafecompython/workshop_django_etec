from django.contrib import admin

# Register your models here.
from .models import Postagem, Comentario

admin.site.register(Postagem)
admin.site.register(Comentario)