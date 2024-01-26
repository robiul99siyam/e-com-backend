from rest_framework import serializers
from .models import Feature_product,new_arrevals


#----------- feature product --------------->

class Feature_productSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Feature_product
        fields="__all__"


#-------------- new arrevals ---------------------->


class New_ArrevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_arrevals
        fields = '__all__'