from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializer import UsarioSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsarioSerializer

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = Usuario.objects.all()
#    serializer_class = UserSerializer
