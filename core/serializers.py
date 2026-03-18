from rest_framework import serializers
from .models import Employee , Attandance

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
    
    def validate_employee_id(self, value):
        if self.instance and self.instance.employee_id == value:
            return value

        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("Employee ID already exists.")
        
        return value
    
    def validate_email(self, value):
        value = value.lower().strip()

        if self.instance and self.instance.email == value:
            return value

        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")

        return value

class AttandanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)

    class Meta:
        model = Attandance
        fields = '__all__'