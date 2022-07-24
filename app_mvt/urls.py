from django.urls import path
from .views import PaginaInicialView, clienteView, ClienteCreate, ClienteUpdate, ClienteDelete
from . import views

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='inicio'),
    path('cliente/<int:id>', views.clienteView, name='cliente'),
    path('cadastrar/', ClienteCreate.as_view(), name='cadastrar'),
    path('editar/<int:pk>/', ClienteUpdate.as_view(), name='editar/'),
    path('deletar/<int:pk>/', ClienteDelete.as_view(), name='deletar/'),
]