from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentModelSerializer, StudentSerializer
from .models import Student_Two
from rest_framework.views import APIView

# Create your views here.

# @api_view(['GET'])
# def hello_api(request):
#     if request.method == 'GET':
#         return Response({'msg': 'It is get api'})

@api_view(['POST', 'GET'])
def hello_api(request):
    if request.method == 'GET':
        return Response({'msg': 'It is get api'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'It is post api', 'data': request.data})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id != None:
            stu = Student_Two.objects.get(id = id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        
        else:
            stu = Student_Two.objects.all()
            serializer = StudentModelSerializer(stu, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Saved!'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student_Two.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student_Two.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student_Two.objects.get(pk = id)
        stu.delete()
        return Response({'msg': 'Data Deleted!'})


class StudentAPI(APIView):
    def get(self, request, pk = None, format=None):
        id = pk
        if id != None:
            stu = Student_Two.objects.get(id = id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        
        else:
            stu = Student_Two.objects.all()
            serializer = StudentModelSerializer(stu, many=True)
            return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Saved!'})
        return Response(serializer.errors)

    def put(self, request, pk = None, format = None):
        id = pk
        stu = Student_Two.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!'})
        return Response(serializer.errors)

    def patch(self, request, pk=None, format = None):
        # id = request.data.get('id')
        id = pk
        stu = Student_Two.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!'})
        return Response(serializer.errors)

    def delete(self, request, pk=None, format = None):
        # id = request.data.get('id')
        id = pk
        stu = Student_Two.objects.get(pk = id)
        stu.delete()
        return Response({'msg': 'Data Deleted!'})
