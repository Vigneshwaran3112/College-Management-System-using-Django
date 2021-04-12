from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "College Management"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to MEC Admin Portal"


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'email', 'website')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'batch_id', 'year_from', 'year_to')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'sem')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'department', 'college')
    list_display_links = ('college',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sec_id', 'section')

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'designation_id', 'designation')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff_id', 'name', 'designation', 'department')
    list_display_links = ('designation', 'department')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'register_no', 'name', 'section', 'department', 'sem', 'batch')
    list_display_links = ('id','section', 'department', 'sem', 'batch')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'sem', 'department', 'staff')
    list_display_links = ('sem', 'department', 'staff')

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'sem', 'student_register_no', 'subject', 'department', 'mark')
    list_display_links = ('id','sem', 'student_register_no', 'subject', 'department')

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'sem', 'student_register_no', 'department', 'cgpa')
    list_display_links = ('id','sem', 'student_register_no', 'department')
