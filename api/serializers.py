from .models import *
from rest_framework import serializers


class HostelerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hosteler
        fields = '__all__'


class MessBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessBill
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = '__all__'