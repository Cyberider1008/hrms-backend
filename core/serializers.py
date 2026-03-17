from rest_framework import serializers
from .models import Employee , Attandance

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

class AttandanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)

    class Meta:
        model = Attandance
        fields = '__all__'