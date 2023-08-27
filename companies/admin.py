from django.contrib import admin
from companies.models import Employee,Company
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','phone','about','position','company']
admin.site.register(Employee,EmployeeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','about','type','active']
admin.site.register(Company,CompanyAdmin)
