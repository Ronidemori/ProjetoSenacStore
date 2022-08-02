from django.urls import path
from Store import  views


urlpatterns = [
    path('',views.index ,name='index'),
    path('departamentos/',views.Departamentos, name='departamentos'),
    path('categorias/<int:id>',views.Categorias, name='categorias'),
    path('produtos/<int:id>',views.Produtos,name= 'produtos'),
]
