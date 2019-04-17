from django.shortcuts import render, get_object_or_404
from .models import Postagem, Comentario
from .forms import ComentarioForm

# Create your views here.
def home(request):
    posts = Postagem.objects.all()

    return render(request, 'blog/home.html', {'posts':posts})

def postagem(request, pk):
    form = ComentarioForm()
    post = get_object_or_404(Postagem, pk=pk)
    coments = Comentario.objects.filter(post_ref=post)
    context = {'post': post, 'form': form, 'coments': coments}

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            coment=form.save(commit=False)
            coment.post_ref = post
            coment.save()
            form = ComentarioForm()
            return render (request, 'blog/post_detalhe.html', context)
    else:
        return render(request, 'blog/post_detalhe.html', context)

