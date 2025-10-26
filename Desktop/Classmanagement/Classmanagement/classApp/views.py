from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Teacher
from .serializers import StudentSerializers, TeacherSerializers


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_serializer = StudentSerializers(students, many=True)
        return Response(student_serializer.data)

    if request.method == 'POST':
            student_serializer = StudentSerializers(data=request.data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
        if request.method == 'GET':
            student = Student.objects.get(reg_no=pk)
            serializers = StudentSerializers(student, many=True)
            return Response(serializers.data)

        elif request.method == 'PUT':
            student = Student.objects.filter(reg_no=pk)
            serializer = StudentSerializers(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            student = Student.objects.filter(reg_no=pk)
            if student:
                student.delete()
                return Response(status=204)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        teacher_serializer = TeacherSerializers(teachers, many=True)
        return Response(teacher_serializer.data)
    elif request.method == 'POST':
        teachers = Teacher.objects.all()
        teacher_serializer = TeacherSerializers(teachers, data=request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return Response(teacher_serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    if request.method == 'GET':
        teacher = Teacher.objects.get(teacher_id=pk)
        serializer = TeacherSerializers(teacher, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        teacher = Teacher.objects.filter(teacher_id=pk)
        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        teacher = Teacher.objects.filter(teacher_id=pk)
        if teacher:
            teacher.delete()
            return Response(status=204)
