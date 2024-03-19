from django.db import models
import datetime
# Create your models here.
#model.DateTimeField(auto_now = true, null = false ) => update_at
#model.DateTimeField(auto_now_add = true, null = false ) => Defaul now()
#usamos models.Model para usar los timpos de campos ejemplos variables
class User(models.Model):
    email = models.EmailField(null = True, blank = True) 
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(default= True)
    created_at = models.DateTimeField(default = datetime.datetime.now()) 
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Person (models.Model):
    firstname = models.CharField(max_length = 20) 
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField(null = True)
    ident_exp_city = models.IntegerField(null = True)
    address = models.CharField(max_length = 150, blank = True)
    mobile = models.CharField(max_length = 50, blank = True)
    ident_number = models.CharField(max_length = 12, blank = True) 
    id_user = models.IntegerField(null = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
    
class Students(models.Model):
    code = models.CharField(max_length = 20)
    status = models.BooleanField(null = True, blank = True, default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class identification_types(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip =  models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class city(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_dept = models.IntegerField(null = True) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class departments(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_country = models.IntegerField(null = True) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class countries(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)