from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import views, response
from apps.basta.serializers import IstorijaZalivanjaSerializer, TrenutniUsloviSerializer, PodaciSaSenzoraSerializer, RelaySerializer
from apps.basta.models import ArhivskaTabela, DnevnaTabela
import os, time, serial
#from apps.basta import relejon as rl

#komunikacija = serial.Serial("/dev/ttyUSB0", 115200)
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
        vlaznost_zemljista = serializer.validated_data['vlaznost_zemljista']
        kisa = serializer.validated_data['kisa']
        zalivanje = serializer.validated_data['zalivanje']
        otvoren_prozor = serializer.validated_data['otvoren_prozor']
        ventilator = serializer.validated_data['radi_ventilator']

        DnevnaTabela.objects.create(
            temperatura=temperatura,
            vlaznost_vazduha=vlaznost_vazduha,
            kisa=kisa,
            vlaznost_zemljista=vlaznost_zemljista,
            zalivanje=zalivanje,
            radi_ventilator=ventilator,
            otvoren_prozor=otvoren_prozor
        )

        print(serializer.validated_data)
        return response.Response(serializer.data)

class RelayOnView(views.APIView):

    def post(self, request):
        serializer = RelaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        turn_on = serializer.validated_data['ukljuci']

        def komanda(sifra):
            time.sleep(5)
            # komunikacija.write(str(sifra).encode("UTF-8"))

        komanda(turn_on)
        #if turn_on == 0:
            #rl.komanda(4)
            #rl.komanda(2)
            #rl.komanda(0)
        #else:
           # os.system("python apps/basta/relejoff.py")
           # return response.Response(serializer.data)
        return response.Response(serializer.data)