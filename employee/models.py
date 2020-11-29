from django.db import models


# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    department = models.CharField(max_length=50, blank=False, null=False)


class Employee(models.Model):
    manager_id = models.ForeignKey(Manager, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    department = models.CharField(max_length=50, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)