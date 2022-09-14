from asyncore import read
from dataclasses import fields
from pyexpat import model
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student_Three


def name_starts_with_r(value):
    if value[0].lower() == 'r':
        raise serializers.ValidationError('Name cannot starts with r')



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators =[name_starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    
    def create(self, validate_data):
        return Student_Three.objects.create(**validate_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance

    
    # Field Level Validation 

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats are full')
        return value
    
    
    # Object Level Validation 
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'murtaza' and ct.lower() != 'karachi':
            raise serializers.ValidationError('City must be Karachi')
        return data


# Model Serializer 
class StudentModelSerializer(serializers.ModelSerializer):
    # roll = serializers.CharField(read_only = True)
    
    class Meta:
        model = Student_Three
        fields = ['id', 'name', 'city', 'roll']
        # read_only_fields = ['roll']
        # extra_kwargs = {'roll': {'read_only': True}}

    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('Seats are full')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'murtaza' and ct.lower() != 'karachi':
            raise serializers.ValidationError('City must be karachi')
        return data 