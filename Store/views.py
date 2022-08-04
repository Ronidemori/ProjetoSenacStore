from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Categoria,Departamento,Categoria,Produto
from Store.models import Produto

# Create your views here.
def index(request):
    meu_nome= ' bertano da silva'
    sexo = 'M'
    context = {'nome': meu_nome,'artigo':'o' if sexo == 'M' else 'a'
    }
    return render (request,'index.html',context)  

def teste(request):
  # depto =  ['Casa','Informatica','Telefonia'] 
    depto = Departamento.objects.all() 
    context = {'departamentos': depto}   
    return render( request,'teste.html',context)

def Departamentos(request):
  # depto =  ['Casa','Informatica','Telefonia'] 
    depto = Departamento.objects.all() 
    context = {'departamentos': depto}   
    return render( request,'departamentos.html',context)

def Categorias(request,id):
    lista_categorias = Categoria.objects.filter(departamento_id =id ) 
    depto = Departamento.objects.get(id = id)
    context = {
                'categorias': lista_categorias,
                'departamento':depto
              }   
    return render( request,'categorias.html',context) 


    
def Produtos(request,id):
    lista_produtos = Produto.objects.filter(categoria_id = id) 
    context = {'produtos': lista_produtos}   
    return render( request,'produtos.html',context)
    
   



