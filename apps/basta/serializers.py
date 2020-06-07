from rest_framework import serializers
from apps.basta.models import ArhivskaTabela, DnevnaTabela

class IstorijaZalivanjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArhivskaTabela
        fields = ['datum', 'broj_zalivanja', 'prosecna_temperatura', 'prosecna_vlaznost_vazduha',
                  'prosecna_vlaznost_zemljista', 'prosek_kisa']


class TrenutniUsloviSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnevnaTabela
        fields = ['datum', 'temperatura', 'vlaznost_vazduha', 'vlaznost_zemljista', 'kisa', 'zalivanje',
                  'otvoren_prozor', 'radi_ventilator']

class PodaciSaSenzoraSerializer(serializers.Serializer):
    temp = serializers.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_vazduha = serializers.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_zemljista = serializers.DecimalField(max_digits=14, decimal_places=2)
    kisa = serializers.DecimalField(max_digits=15, decimal_places=2)
    zalivanje = serializers.BooleanField(default=False)
    otvoren_prozor = serializers.BooleanField(default=False)
    radi_ventilator = serializers.BooleanField(default=False)

class RelaySerializer(serializers.Serializer):
    ukljuci = serializers.IntegerField()