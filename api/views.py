from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Course, Enrollment, Assignment, Submission
from .serializers import (
    UserSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    AssignmentSerializer,
    SubmissionSerializer,
)

# ✅ User registration / listing
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Courses
from rest_framework.parsers import MultiPartParser, FormParser

class CourseView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        courses = Course.objects.all()
        return Response(CourseSerializer(courses, many=True).data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Enrollments
class EnrollmentView(APIView):
    def get(self, request, user_id=None):
        if user_id:
            enrollments = Enrollment.objects.filter(student_id=user_id)
        else:
            enrollments = Enrollment.objects.all()
        return Response(EnrollmentSerializer(enrollments, many=True).data)

    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Assignments
class AssignmentView(APIView):
    def get(self, request, course_id=None):
        if course_id:
            assignments = Assignment.objects.filter(course_id=course_id)
        else:
            assignments = Assignment.objects.all()
        return Response(AssignmentSerializer(assignments, many=True).data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Submissions
class SubmissionView(APIView):
    def get(self, request, assignment_id=None):
        if assignment_id:
            submissions = Submission.objects.filter(assignment_id=assignment_id)
        else:
            submissions = Submission.objects.all()
        return Response(SubmissionSerializer(submissions, many=True).data)

    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
