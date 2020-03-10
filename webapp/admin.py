from django.contrib import admin
from .models import EmpModelForm

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['EmpId','EmpName','EmpSal','EmpLoc']
admin.site.register(EmpModelForm,EmpAdmin)