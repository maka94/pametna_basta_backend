from rest_framework import serializers
from apps.basta.models import ArhivskaTabela, DnevnaTabela

class IstorijaZalivanjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArhivskaTabela
        fields = ['datum', 'broj_zalivanja', 'prosecna_temperatura', 'prosecna_vlaznost_vazduha', 'prosecni_vazdusni_pritisak',
                  'prosecna_vlaznost_zemljista']


class TrenutniUsloviSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnevnaTabela
        fields = ['datum', 'temperatura', 'vlaznost_vazduha', 'vazdusni_pritisak', 'vlaznost_zemljista']

class PodaciSaSenzoraSerializer(serializers.Serializer):
    temp = serializers.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_vazduha = serializers.DecimalField(max_digits=15, decimal_places=2)
    vazdusni_pritisak = serializers.DecimalField(max_digits=15, decimal_places=2)
    vlaznost_zemljista = serializers.DecimalField(max_digits=14, decimal_places=2)

class RelaySerializer(serializers.Serializer):
    ukljuci = serializers.BooleanField(default=False)