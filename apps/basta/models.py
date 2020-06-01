from django.db import models
import datetime

class DnevnaTabela(models.Model):
    datum = models.DateField(default=datetime.date.today)
    temperatura = models.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_vazduha = models.DecimalField(max_digits=15, decimal_places=2)
    vazdusni_pritisak = models.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_zemljista = models.DecimalField(max_digits=15, decimal_places=2)

class ArhivskaTabela(models.Model):
    datum = models.DateField(default=datetime.date.today)
    broj_zalivanja = models.IntegerField(default=0)
    prosecna_temperatura = models.DecimalField(max_digits=15, decimal_places=2)
    prosecna_vlaznost_vazduha = models.DecimalField(max_digits=15, decimal_places=2)
    prosecni_vazdusni_pritisak = models.DecimalField(max_digits=15, decimal_places=2)
    prosecna_vlaznost_zemljista = models.DecimalField(max_digits=15, decimal_places=2)
