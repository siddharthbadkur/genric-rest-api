from .models import StudentModel
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ["id",'username','first_name','last_name','email','password']