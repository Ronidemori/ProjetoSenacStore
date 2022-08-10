from django.urls import path
from Store import  views


urlpatterns = [
    path('',views.index ,name='index'),
    path('departamentos/',views.Departamentos, name='departamentos'),
    path('categorias/<int:id>',views.Categorias, name='categorias'),
    path('produtos/<int:id>',views.Produtos,name= 'produtos'),
    path('produto_detalhe/<int:id>',views.produto_detalhe,name =" produto")
    path('institucional/'views.institucional,name = ' institucional')
    path('contato'/views.contato, name ='contato')

]
