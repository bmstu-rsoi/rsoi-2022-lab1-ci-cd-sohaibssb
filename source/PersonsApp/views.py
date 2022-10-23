
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Person
from .serializers import PersonsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from django.http import HttpResponse



@api_view(['GET','POST'])
def listPersons(request,format=None):
    if request.method=='GET':
        id_persons = Person.objects.all()
        serializer = PersonsSerializer(id_persons, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=PersonsSerializer(data=request.data)
        if serializer.is_valid():
            IDper=serializer.save()
            response=Response(status=status.HTTP_201_CREATED)
            response['Location']='/api/v1/persons/{IDperson}'.format(IDperson=IDper.id)
            return response
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH','DELETE'])
def aSpecificPersons(request,id,format=None):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=PersonsSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='PATCH':
        serializer=PersonsSerializer(person,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
