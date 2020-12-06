from rest_framework import serializers
from employee.models import Manager, Employee
from django.contrib.auth.models import User


class Managerserialize(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"


class Employeeserialize(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class Userserialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
