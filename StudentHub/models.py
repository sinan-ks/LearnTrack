from django.db import models

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=200, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class Student(models.Model):

    student_name = models.CharField(max_length=200)

    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    gender=models.CharField(max_length=20, null=True)

    age=models.IntegerField(null=True)

    place = models.CharField(max_length=200)

    mobile_number = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    qualification = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        
        return self.student_name