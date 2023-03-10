from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    ordering = ['lastname']

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.lastname}'
    
class Course(models.Model):
    name = models.CharField(max_length=25)
    students = models.ManyToManyField(Student, related_name="courses")
    teacher= models.ForeignKey(Teacher, related_name="course", blank=True, null=True, on_delete=models.SET_NULL)
    
    #sirve para crear una propiedad que se pueda usar en el serializer
    @property
    def quantity(self):
        return self.students.count()
    
    def __str__(self):
        return f'{self.name}'    

