from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_us
from .serializer import ContactSerializer
#--------------- Contact Us -------------------->

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact_us.objects.all()
    serializer_class = ContactSerializer
    