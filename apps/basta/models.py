from django.db import models
import datetime

class DnevnaTabela(models.Model):
    datum = models.DateField(default=datetime.date.today)
    temperatura = models.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_vazduha = models.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_zemljista = models.DecimalField(max_digits=15, decimal_places=2)
    kisa = models.DecimalField(max_digits=15, decimal_places=2)
    zalivanje = models.BooleanField(default=False)
    otvoren_prozor = models.BooleanField(default=False)
    radi_ventilator = models.BooleanField(default=False)

class ArhivskaTabela(models.Model):
    datum = models.DateField(default=datetime.date.today)
    broj_zalivanja = models.IntegerField(default=0)
    prosecna_temperatura = models.DecimalField(max_digits=15, decimal_places=2)
    prosecna_vlaznost_vazduha = models.DecimalField(max_digits=15, decimal_places=2)
    prosecna_vlaznost_zemljista = models.DecimalField(max_digits=15, decimal_places=2)
    prosek_kisa = models.DecimalField(max_digits=15, decimal_places=2)
