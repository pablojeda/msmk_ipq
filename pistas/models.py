from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)


class PistasPadel(models.Model):
    numero = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    indoor = models.BooleanField(default=False)


class Disponibilidad(models.Model):
    date = models.DateTimeField()
    is_free = models.BooleanField(default=True)
    pista = models.ForeignKey(PistasPadel, on_delete=models.CASCADE)
