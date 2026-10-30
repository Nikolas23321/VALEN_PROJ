from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Casa(models.Model):
    numero = models.CharField(max_length=5)
    titulo = models.CharField(max_length=100)
    hospedes = models.PositiveIntegerField()
    quartos = models.PositiveIntegerField()
    localizacao = models.CharField(
        max_length=150,
        default="Litoral do Rio Grande do Norte"
    )
    descricao = models.TextField()
    imagem = models.URLField()
    em_destaque = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=1)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="casas"
    )

    class Meta:
        ordering = ['ordem', 'numero']

    def __str__(self):
        return f"{self.numero} - {self.titulo}"


class Objetivo(models.Model):
    numero = models.CharField(max_length=5)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['ordem', 'numero']

    def __str__(self):
        return f"{self.numero} - {self.titulo}"
