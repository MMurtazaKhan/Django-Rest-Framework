from ast import Delete
import imp
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Student_Three
from .serializers import StudentModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

############### MODEL MIXINS #################################

class StudentList(GenericAPIView, ListModelMixin):
    
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetreive(GenericAPIView, RetrieveModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


############## COMBINE MODEL MIXINS ##############################

# List and Create API 
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retreive, Update and Delete - pk Required 
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


################### APIVIEWS #######################################

class StudentList(ListAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentCreate(CreateAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer


################## COMBINE APIVIEWS ##################################

class StudentListCreate(ListCreateAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetreiveDestroy(RetrieveDestroyAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetreiveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student_Three.objects.all()
    serializer_class = StudentModelSerializer