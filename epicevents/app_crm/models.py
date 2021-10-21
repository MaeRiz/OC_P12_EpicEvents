from django.db import models
from app_management.models import CustomUser


class Client(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    prospect = models.BooleanField(default=True)
    sale_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    compagny = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payement_due = models.DateTimeField()
    stat = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    stat = models.BooleanField(default=True)
    attendees = models.IntegerField()
    notes = models.TextField(max_length=2048)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
