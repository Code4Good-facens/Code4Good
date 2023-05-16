from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default = 'C',
        max_length = 1,
        choices= (
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {Pedido.pk}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    preco = models.FloatField()
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.pedido}'

"""
        ItemPedido:
            pedido - FK pedido
            produto - Char
            produto_id - Int
            variacao - Char
            variacao_id - Int
            preco - Float
            preco_promocional - Float
            quantidade - Int
            imagem - Char
"""