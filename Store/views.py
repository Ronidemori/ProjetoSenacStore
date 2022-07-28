from  django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento,Categoria,
from Store.models import Produtos

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

def Categorias(request):
    list_categorias =  Categoria.objects.all() 
    context = {'categorias': list_categorias}   
    return render( request,'categorias.html',context)    
    
def Produtos(request):
    lista_produtos = Produtos.objects.all() 
    context = {'produtos':list_produtos}   
    return render( request,'produtos.html',context)
    
   



