from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, serializer, permissions


class ProspectViewSet(viewsets.ModelViewSet):

    search_fields = ['firstname', 'lastname', 'email', 'compagny',]
    filter_backends = (filters.SearchFilter,)
    queryset = models.Client.objects.filter(prospect=True)
    serializer_class = serializer.ClientSerializer
    permission_classes = (IsAuthenticated, permissions.ProspectPermissions,)

    def create(self, request):
        data = request.data.copy()
        data['prospect'] = True

        serialized_data = serializer.ClientSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        client = get_object_or_404(models.Client, pk=pk)

        data = request.data.copy()

        if data['prospect'] == False:
            data['sale_contact'] = request.user.pk

        serialized_data = serializer.ClientSerializer(
            data=data, instance=client
        )
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data)


class ClientViewSet(viewsets.ModelViewSet):

    search_fields = ['firstname', 'lastname', 'email', 'compagny',]
    filter_backends = (filters.SearchFilter,)
    queryset = models.Client.objects.filter(prospect=False)
    serializer_class = serializer.ClientSerializer
    permission_classes = (IsAuthenticated, permissions.ClientPermissions)

    def get_queryset(self):
        if self.request.user.role == 'SUPPORT':
            return models.Client.objects.filter(
                contract__event__support_contact=self.request.user.pk
            )
        return models.Client.objects.filter(sale_contact=self.request.user.pk)

    def create(self, request):
        data = request.data.copy()
        data['sale_contact'] = request.user.pk
        data['prospect'] = False

        serialized_data = serializer.ClientSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class ContractViewSet(viewsets.ModelViewSet):

    search_fields = ['amount', 'created_time',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = serializer.ContractSerializer
    permission_classes = (IsAuthenticated, permissions.ContractPermissions)

    def get_queryset(self):
        if self.request.user.role == 'SUPPORT':
            return models.Contract.objects.filter(
                client=self.kwargs['client_pk'],
                event__support_contact=self.request.user.pk
            )
        return models.Contract.objects.filter(client=self.kwargs['client_pk'])

    def create(self, request, client_pk=None):
        data = request.data.copy()
        data['client'] = client_pk

        serialized_data = serializer.ContractSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class EventViewSet(viewsets.ModelViewSet):

    search_fields = ['date',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = serializer.EventSerializer
    permission_classes = (IsAuthenticated, permissions.EventPermissions)

    def get_queryset(self):
        return models.Event.objects.filter(
            contract=self.kwargs['contract_pk'],
            support_contact=self.request.user.pk
        )

    def create(self, request, client_pk=None, contract_pk=None):
        data = request.data.copy()
        data['contract'] = contract_pk

        serialized_data = serializer.EventSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
