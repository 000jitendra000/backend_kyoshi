from django.contrib import admin
from .models import User, Course, Enrollment, Assignment, Submission

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_teacher", "is_student")
    list_filter = ("is_teacher", "is_student")
    search_fields = ("username", "email")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "teacher")
    search_fields = ("title",)
    list_filter = ("teacher",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "enrolled_on")
    list_filter = ("course",)
    search_fields = ("student__username", "course__title")


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "due_date")
    list_filter = ("course",)
    search_fields = ("title", "course__title")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "assignment", "student", "grade", "submitted_on")
    list_filter = ("assignment", "grade")
    search_fields = ("student__username", "assignment__title")

