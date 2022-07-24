from django.db import models

STATUS_TIPO = (
    ('Matriz', 'Matriz'),
    ('Filial', 'Filial'),
)

STATUS_ATIVO = (
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
)

class Clientes(models.Model):
    razao_social = models.CharField(max_length=500)
    cnpj = models.CharField(unique=True, max_length=14)
    tipo = models.CharField(
        max_length=6,
        choices=STATUS_TIPO,
    )
    cidade = models.CharField(max_length=30)
    ativo = models.CharField(
        max_length=7,
        choices=STATUS_ATIVO,
    )

    class Meta:
        managed = False
        db_table = 'clientes'

    def __str__(self):
            return 'Empresa: {},\
                    CNPJ: {},\
                    Tipo: {},\
                    Cidade: {},\
                    Ativo: {}'.\
                format(self.razao_social,\
                       self.cnpj,\
                       self.tipo,\
                       self.cidade,\
                       self.ativo)