from rest_framework import serializers
from .models import Teacher, Student, Course
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(SignupSerializer, self).create(validated_data)
    class Meta:
        model= User
        fields=['username', 'password']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']

class TeacherSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(many=True)
    class Meta:
        model = Teacher
        fields = ['id','name','lastname','date_of_birth','age','course']

class CourseSerializer(serializers.ModelSerializer):
    number_of_students = serializers.ReadOnlyField(source='quantity') #sirve para usar la propiedad que tenga el modelo
    class Meta:
        model= Course
        fields = ['id', 'name', 'number_of_students', 'teacher', 'students']
        

class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Student
        fields = ['id','name','lastname','date_of_birth','age','courses']