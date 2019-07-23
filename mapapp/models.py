from django.db import models
import datetime

# Create your models here.
# 1 to 1	college-library
# 1 to m	library-book
# m to 1	book-student
# m to m	library-student


class College(models.Model):
    name=models.CharField(max_length=33)
    staff=models.IntegerField()
    Email=models.EmailField()
    address=models.CharField(max_length=33)

    class meta:
        db_table="college_info"


class Library(models.Model):
    incharge=models.CharField(max_length=33)
    staff=models.IntegerField()
    Email=models.EmailField()
    address=models.CharField(max_length=33)
    college = models.OneToOneField(College, on_delete=models.CASCADE)

    class meta:
        db_table="Library_info"

class Student(models.Model):
    name=models.CharField(max_length=33)
    branch=models.CharField(max_length=33)
    roll_no=models.IntegerField()
    DOB=models.DateTimeField()  # datetime.datetime.now()
    Email=models.EmailField()
    address=models.CharField(max_length=33)
    library=models.ManyToManyField(Library)
# s1 = Student(name='sas', branch='shfbks', roll_no=85, DOB=datetime.datetime.now(), Email='svd@s.com',address='fjskdf')s1.library=
    class meta:
        db_table="student_info"

class Book(models.Model):
    name=models.CharField(max_length=33)
    publisher=models.CharField(max_length=33)
    pub_date=models.DateField()
    library=models.ForeignKey(Library,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
# datetime.datetime.now()
    class meta:
        db_table="Book_info"

