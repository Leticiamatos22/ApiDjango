from django.db import models

class Status(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def __str__(self):
        return f"Status: {self.id}"
