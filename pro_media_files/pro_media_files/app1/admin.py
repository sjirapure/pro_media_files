from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','name','salary','mail','city','image','resume']
admin.site.register(Employee,EmployeeAdmin)
