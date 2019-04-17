from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Postagem(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens', blank=True, null=True)
    post_texto = models.TextField()
    data_publicacao = models.DateTimeField('data de publicação', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Postagens'
        ordering = ['-data_publicacao']
    
    def __str__(self):
        return self.post_titulo


class Comentario(models.Model):
    post_ref = models.ForeignKey('Postagem', on_delete=models.CASCADE)
    coment_autor = models.CharField(max_length=40)
    coment_texto = models.TextField()
    coment_publicacao = models.DateTimeField('data de publicação', default=timezone.now)

    class Meta:
        verbose_name = 'Comentário'
        ordering = ['-coment_publicacao']

    def __str__(self):
        return self.coment_autor
    