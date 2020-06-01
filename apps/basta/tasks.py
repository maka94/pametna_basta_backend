from celery import shared_task
import requests, datetime
from apps.basta.models import DnevnaTabela, ArhivskaTabela

@shared_task
def test():
    return 1

@shared_task
def get_weatherAPI_data():
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}'.format('Beograd',
     '4e5756bc68c875c90215ba8f05e32fe3','metric'))
    data_json = data.json()
    temperatura = data_json['main']['temp']
    vlaznost_vazduha = data_json['main']['humidity']
    vazdusni_pritisak = data_json['main']['pressure']
    clouds = data_json['clouds']['all']
    DnevnaTabela.objects.create(temperatura=temperatura, vlaznost_vazduha=vlaznost_vazduha,
                                vazdusni_pritisak=vazdusni_pritisak, vlaznost_zemljista=clouds)

@shared_task
def daily_averages():
    queryset = DnevnaTabela.objects.all()

    temperatura = 0
    vlaznost_vazduha = 0
    vazdusni_pritisak = 0
    vlaznost_zemljista = 0
    datum = datetime

    for entry in queryset:
        temperatura += entry.temperatura
        vlaznost_vazduha += entry.vlaznost_vazduha
        vazdusni_pritisak += entry.vazdusni_pritisak
        vlaznost_zemljista += entry.vlaznost_zemljista
        datum = entry.datum

    prosecna_temp = temperatura / queryset.count()
    prosecna_vlaznost_vazduha = vlaznost_vazduha / queryset.count()
    prosecni_vazdusni_pritisak = vazdusni_pritisak / queryset.count()
    prosecna_vlaznost_zemljista = vlaznost_zemljista / queryset.count()

    ArhivskaTabela.objects.create(datum= datum, prosecna_temperatura=prosecna_temp,
                                  prosecna_vlaznost_vazduha= prosecna_vlaznost_vazduha,
                                  prosecni_vazdusni_pritisak=prosecni_vazdusni_pritisak,
                                  prosecna_vlaznost_zemljista=prosecna_vlaznost_zemljista)