from functools import partial
import json
from turtle import st
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer, StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View




# Class Based API 
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request,  *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)

            id = python_data.get('id', None)

            if id is not None:
                stu = Student.objects.get(id = id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data saved'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'data deleted'}
        data = JSONRenderer().render(res)
        return HttpResponse(data, content_type = 'application/json')





# Create your views here.

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

# query Set - All data 
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()

            res = {
                'msg': 'Data has been saved'
            }
            return JsonResponse(res)


# CRUD operation APis
@csrf_exempt
def get_student(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data saved'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')

    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')

    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'data deleted'}
        data = JSONRenderer().render(res)
        return HttpResponse(data, content_type = 'application/json')




# Model Serializer 
@method_decorator(csrf_exempt, name='dispatch')
class StudentModelAPI(View):
    def get(self, request,  *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)

            id = python_data.get('id', None)

            if id is not None:
                stu = Student.objects.get(id = id)
                serializer = StudentModelSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

            stu = Student.objects.all()
            serializer = StudentModelSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentModelSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data saved'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentModelSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            data = JSONRenderer().render(res)
            return HttpResponse(data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'data deleted'}
        data = JSONRenderer().render(res)
        return HttpResponse(data, content_type = 'application/json')



