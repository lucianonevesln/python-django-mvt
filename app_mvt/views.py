from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Clientes
from django.urls import reverse_lazy
from django.http import HttpResponse


#################### Lista de Clientes ####################

class PaginaInicialView(ListView):
    template_name = 'inicio.html'
    model = Clientes


################## Informacoes do Cliente #################

def clienteView(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    return render(request, 'cliente.html', {'cliente': cliente})


#################### Cadastro ####################

class ClienteCreate(CreateView):
    model = Clientes
    fields = '__all__'
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('inicio')


#################### Alteracao ###################

class ClienteUpdate(UpdateView):
    model = Clientes
    fields = ['razao_social', 'tipo', 'cidade', 'ativo']
    template_name = 'editar.html'
    success_url = reverse_lazy('inicio')


#################### Exclusao ####################

class ClienteDelete(DeleteView):
    model = Clientes
    fields = '__all__'
    template_name = 'deletar.html'
    success_url = reverse_lazy('inicio')