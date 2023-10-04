from django.db import models

# Create your models here.
class TiposExames(models.Model):
    tipo_choices =(
        ('I','Exame de Imagem'),
        ('S', 'Exame de sangue')
    )
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)
    horario_inicial= models.IntegerField()
    horario_final= models.IntegerField()

    def _str_(self):
        return self.nome
