from rest_framework import serializers
from basics.models import T_1, T_2, T_3


class T1Serializer(serializers.ModelSerializer):
    class Meta:
        model = T_1
        fields = ['id', 'name']


class T2Serializer(serializers.ModelSerializer):
    class Meta:
        model = T_2
        fields = ['id', 'name']

class T3Serializer(serializers.ModelSerializer):
    class Meta:
        model = T_3
        fields = ['id', 'name']
