from django.db import models
from django.db.models.query_utils import refs_expression
from pkg_resources import require
from app_management.models import CustomUser


class Client(models.Model):
    firstname = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)
    prospect = models.BooleanField(default=True)
    sale_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    compagny = models.CharField(max_length=128, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contract')
    amount = models.IntegerField()
    payement_due = models.DateTimeField()
    stat = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='event')
    support_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    stat = models.BooleanField(default=True)
    attendees = models.IntegerField()
    notes = models.TextField(max_length=2048)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
