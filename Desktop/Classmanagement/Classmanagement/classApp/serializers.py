from rest_framework import serializers
from classApp.models import *

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['reg_no', 'name', 'address', 'email', 'gender','contact']

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id','Name','email','contact','salary','is_lecture']
