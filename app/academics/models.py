from django.db import models
import datetime
# Create your models here.
#model.DateTimeField(auto_now = true, null = false ) => update_at
#model.DateTimeField(auto_now_add = true, null = false ) => Defaul now()
#usamos models.Model para usar los timpos de campos ejemplos variables
class User(models.Model):
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True, default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Person(models.Model):
    firstname = models.CharField(max_length = 20) 
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length = 12, blank = True)

    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Student(models.Model):
    code = models.CharField(max_length = 50) 
    id_person = models.IntegerField()
    status = models.BooleanField(null = True, blank = True, default = True) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Identification_type(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 100) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class City(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_dept = models.IntegerField() 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Departament(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_country = models.IntegerField() 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Country(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)