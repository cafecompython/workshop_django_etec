from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('postagem/<int:pk>/', views.postagem, name='postagem')
]
