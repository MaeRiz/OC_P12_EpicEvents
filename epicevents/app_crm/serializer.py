from rest_framework import serializers

from .models import Client, Event, Contract


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only__fields = (
            'id',
            'sale_contact',
            'created_time',
            'updated_time'
        )


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        read_only__fields = ('id', 'created_time', 'updated_time')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only__fields = ('id', 'created_time', 'updated_time')
