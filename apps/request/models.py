from django.db import models
from apps.users.models import User

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField('Fecha de Peticion', auto_now=False, auto_now_add=True)
    frase_enviada = models.TextField('Body de Peticion')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField("Respuesta peticion")
    response_status = models.IntegerField("Status peticion")
    conversation_id = models.UUIDField("ID conversacion", null=True)
    algorithm = models.CharField(max_length=100)
    site_id = models.CharField(max_length=10, null=True)
    bot_name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Peticion'
        verbose_name_plural = 'Peticiones'
        ordering = ['date']

    def __str__(self):
        return str(self.id)

        