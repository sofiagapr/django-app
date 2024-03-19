from django.contrib import admin
from.models import User, Person, Student, Identification_type, City, Department, Country
# Register your models here.

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Identification_type)
admin.site.register(City)
admin.site.register(Department)
admin.site.register(Country)