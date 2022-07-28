from django.urls import path
from Store import  views


urlpatterns = [
    path('',views.index ,name='index'),
    path('teste/',views.teste,name='teste'),
    path('departamentos/',views.Departamentos, name='departamentos'),
    path('categorias/',views.Categorias, name='categorias'),
    path('produtos/',views.produtos,name= 'produtos'),
]