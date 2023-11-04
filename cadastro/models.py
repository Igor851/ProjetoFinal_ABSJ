from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.IntegerField(
        validators=[
            MaxValueValidator(99),  # Define o valor máximo como 99
            MinValueValidator(0)    # Define o valor mínimo como 0
        ]
    )
    email = models.EmailField()
    contato = models.CharField(max_length=11)
    nota1 = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    nota2 = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    nota3 = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    nota4 = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    def __str__(self):
        return self.nome