from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Department
from . models import Course


# Register your models here.
admin.site.register(Department)
admin.site.register(Course)