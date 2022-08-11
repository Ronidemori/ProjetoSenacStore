from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Categoria,Departamento,Categoria,Produto
from Store.models import Produto
from django.core.mail import send_mail

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

def produto_detalhe(request,id):
  produto = Produto.objects.get(id=id)
  context =   {
               'produto :produto'
    
  }
  return render (request,'produto_detalhe.html',context)

def institucional (request):
    return render(request,'institucional.html')    
    
def contato (request):
    return render(request,"contato.html")

def enviar_email(request):
  nome=request.POST [' nome']
  telefone = request.POST ['telefone']
  assunto = request.POST ['assunto']
  mensagem = request.POST [mensagem],

  remetente = request.POST ['email']
  destinatario = ['ronidemori@gmail.com']

  corpo = f"Nome : {nome}\n\Telefone:{telefone}\n Mensagem:{mensagem}"
  try:
       send_mail ( assunto, corpo, remetente, destinatario)
       context = {'msg': 'E-mail enviado com sucesso!'}
  except:
       context = {'msg': 'Erro ao enviar o e-mail !'}
  return render (request, 'contato.html',context)     

    

   



