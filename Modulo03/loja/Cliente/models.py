from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome + ' - ' + str(self.idade)

    class Meta:
        db_table = 'Cliente'
    
