from rest_framework import views, response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from apps.users.serializers import InputRegisterUserSerializer, OutputRegisterUserSerializer, InputLoginUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

User = get_user_model()

class RegisterView(views.APIView):

    def post(self, request):
        input_serializer = InputRegisterUserSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        print(input_serializer.data)
        u = User.objects.create(
            first_name=input_serializer.data['first_name'],
            last_name=input_serializer.data['last_name'],
            username=input_serializer.data['username']
        )
        u.set_password(input_serializer.data['password'])
        u.save()

        output_serializer = OutputRegisterUserSerializer(u)
        return response.Response(output_serializer.data)

class LoginView(views.APIView):
    def post(self, request):
        input_serializer = InputLoginUserSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        if User.objects.filter(username=input_serializer.data['username']).exists():
            u = User.objects.get(username=input_serializer.data['username'])
            if u.check_password(input_serializer.data['password']):
                if Token.objects.filter(user=u).exists():
                    token = Token.objects.get(user=u)
                else:
                    token = Token.objects.create(user=u)
                print(token.key)
                return response.Response({'token': token.key})

        return response.Response({'error': 'Bad credentials'}, status=400)

class LogOutView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(key=request.auth).delete()
        return response.Response("ok")