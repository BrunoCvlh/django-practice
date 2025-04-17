from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request): #criar a função depois de terminar de preencher os models
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
    #no caso dessa função, é importante capturar os valores da interface, criar um dicionário e mostrar os dados do dicionário em uma nova pagina que será criada logo após.

def pagina_teste(request):
    return render(request, 'usuarios/pagina_teste.html')