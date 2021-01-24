from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField()
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    city = models.CharField(max_length=200)