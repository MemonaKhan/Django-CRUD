from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')         # there was an error here

# admin.site.register(Student)


