from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import views, response
from apps.basta.serializers import IstorijaZalivanjaSerializer, TrenutniUsloviSerializer, PodaciSaSenzoraSerializer, RelaySerializer
from apps.basta.models import ArhivskaTabela, DnevnaTabela
import os

User = get_user_model()

class IstorijaZalivanjaView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = ArhivskaTabela.objects.all()
        serializer = IstorijaZalivanjaSerializer(queryset, many=True)
        return response.Response(serializer.data)

class TrenutniUsloviView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = DnevnaTabela.objects.last()
        serializer = TrenutniUsloviSerializer(queryset, many=False)
        return response.Response(serializer.data)

class UpisiPodatkeSaSenzoraView(views.APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PodaciSaSenzoraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        temperatura = serializer.validated_data['temp']
        vlaznost_vazduha = serializer.validated_data['vlaznost_vazduha']
        vazdusni_pritisak = serializer.validated_data['vazdusni_pritisak']
        vlaznost_zemljista = serializer.validated_data['vlaznost_zemljista']

        DnevnaTabela.objects.create(
            temperatura=temperatura,
            vlaznost_vazduha=vlaznost_vazduha,
            vazdusni_pritisak=vazdusni_pritisak,
            vlaznost_zemljista=vlaznost_zemljista
        )

        print(serializer.validated_data)
        return response.Response(serializer.data)

class RelayOnView(views.APIView):

    def post(self, request):
        serializer = RelaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        turn_on = serializer.validated_data['ukljuci']

        if turn_on == True:
            os.system("python apps/basta/relejon.py")
            return response.Response(serializer.data)
        else:
            os.system("python apps/basta/relejoff.py")
            return response.Response(serializer.data)