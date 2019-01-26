from django.db import models

# Create your models here.

class Titulo(models.Model):
    titulo = models.CharField(max_length = 80)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Pergunta(models.Model):
    pergunta = models.CharField(max_length = 200)
    imagens = models.ImageField(upload_to='', blank=True, null=True)
    

    def __str__(self):
        return self .pergunta


class opcoes(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE,blank=True)
    Alternativas = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    


    def __str__(self):
        return self.Alternativas
