from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

from .models import Student

@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET":
        students = User.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # create a new student
    serializer = StudentSerializer(data=request.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, student_id):
    student = get_object_or_404(User, id=student_id)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    deleted_id = str(student.id)
    student.delete()
    return Response({"message": "Student deleted", "_id": deleted_id})

