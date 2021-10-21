from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from . import models, serializer, permissions


class ClientViewSet(viewsets.ModelViewSet):

    search_fields = ['firstname', 'lastname', 'email', 'compagny']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Client.objects.all()
    serializer_class = serializer.ClientSerializer
    permission_classes = (permissions.ClientPermissions)


class ContractViewSet(viewsets.ModelViewSet):

    search_fields = ['amount', 'created_time',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = serializer.ContractSerializer
    permission_classes = (permissions.ContractPermissions)

    def get_queryset(self):
        return models.Contract.objects.filter(client=self.kwargs['client_pk'])

class EventViewSet(viewsets.ModelViewSet):

    serializer_class = serializer.EventSerializer
    permission_classes = (permissions.EventPermissions)

    def get_queryset(self):
        return models.Event.objects.filter(contract=self.kwargs['contract_pk'])
