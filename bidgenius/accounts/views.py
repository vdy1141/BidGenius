from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from .serializers import AccountSerializer,User,CountrySerializer, StateSerializer, CitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import viewsets
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import send_mail
from .models import Country, State, City
from rest_framework import generics


class UserCreate(APIView):
    
    def post(self,request):
        serializer=AccountSerializer(data=request.data)
       # print(request.data)
       # print(serializer)
       # print(request.data['email'])
        if serializer.is_valid():
            print("1")
            user = serializer.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)   
            mail_subject = 'Activate your account.'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = f'http://{current_site.domain}/v1/activate/{uid}/{token}/'
            message = f'Hi {user.username},\n\nPlease use the following link to activate your account:\n{activation_link}'

            to_email = serializer.data.get('email')
            send_mail(mail_subject, message, 'yog.esh.6g1a9@gmail.com', [to_email])
           
            return Response(data={"Data":"Please confirm your email address to complete the registration"})
        else:
            print(serializer.errors) 
            return Response(serializer.errors)
       # return Response(data={"Data":"Please Enter VAlid Data"})

    def get(self,request):
        user=User.objects.all()
        serializer=AccountSerializer(user,many=True)
        return Response(serializer.data)
 
# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class=AccountSerializer
#     queryset=User.objects.all()

class UserActivation(APIView):
    def get(self,request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
           # login(request, user)
            # return redirect('home')
            return Response('Thank you for your email confirmation. Now you can login your account.')
        else:
            return Response('Activation link is invalid!')



class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        country_id = self.request.query_params.get('country_id')
        return State.objects.filter(country_id=country_id)

class CityList(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        state_id = self.request.query_params.get('state_id')
        return City.objects.filter(state_id=state_id)