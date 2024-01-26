from django.shortcuts import render
from .models import Feature_product,new_arrevals
from rest_framework import viewsets
from .serializer import Feature_productSerialzer,New_ArrevalSerializer




#----------------- Featuere product Viewset ------------------------>


class Feature_productViewset(viewsets.ModelViewSet):
    queryset = Feature_product.objects.all()
    serializer_class = Feature_productSerialzer


class New_arrevalViewset(viewsets.ModelViewSet):
    queryset = new_arrevals.objects.all()
    serializer_class = New_ArrevalSerializer
