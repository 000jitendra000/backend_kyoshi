from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view(), name="users"),
    path("courses/", views.CourseView.as_view(), name="courses"),
    path("enrollments/", views.EnrollmentView.as_view(), name="enrollments"),
    path("enrollments/<int:user_id>/", views.EnrollmentView.as_view(), name="enrollments-by-user"),
    path("assignments/", views.AssignmentView.as_view(), name="assignments"),
    path("assignments/<int:course_id>/", views.AssignmentView.as_view(), name="assignments-by-course"),
    path("submissions/", views.SubmissionView.as_view(), name="submissions"),
    path("submissions/<int:assignment_id>/", views.SubmissionView.as_view(), name="submissions-by-assignment"),
]
