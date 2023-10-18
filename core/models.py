from django.db import models

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=40)
    
    def __str__(self)   :
        return self.descricao


class TipoAtuacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self)   :
        return self.descricao   
    class Meta:
        verbose_name_plural     = 'Tipos de Atuacao'

class Pais(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self)   :
        return self.nome
    
    class Meta:
        verbose_name_plural     = 'Paises'

class Produtora (models.Model):
    nome =models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self)   :
        return self.nome
    
class Membro (models.Model):
    nome =models.CharField(max_length=100)
    data_nascimento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

class Filmes (models.Model):
    nome =models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField()
    classificacao = models.IntegerField()
    duracao = models.TimeField()
    Produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name_plural     = 'Filmes'
    def __str__(self)   :
        return f"(self.titulo) {(self.ano)}"

class Atuacao (models.Model):
    filme = models.ForeignKey(Filmes, on_delete=models.PROTECT)
    membro = models.ForeignKey(Membro, on_delete=models.PROTECT)
    tipo_atuacao = models.ForeignKey(TipoAtuacao, on_delete=models.PROTECT)
    personagem = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self)   :
        return f"{self.filme} - {self.membro} ({self.tipo_atuacao})"

   