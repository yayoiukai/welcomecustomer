from django.db import models

# Create your models here.


class Customer(models.Model):
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


class Interest(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    categories = models.CharField(max_length=40)
    target = models.CharField(max_length=20)


class Caterogy(models.Model):
    name = models.CharField(max_length=20)


class Consierge(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)


class Meeting(models.Model):
    location = models.CharField(max_length=20)
    concierge = models.ForeignKey(Consierge)
