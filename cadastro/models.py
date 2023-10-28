from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    email = models.EmailField()
    contato = models.CharField(max_length=11)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    nota3 = models.IntegerField()
    nota4 = models.IntegerField()
    def __str__(self):
        return self.nome