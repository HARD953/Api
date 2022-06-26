from msilib.schema import ListView
from django import views
from django.shortcuts import*
from crud.models import*
from crud.serializers import*
from django.http import HttpResponseGone,JsonResponse
from django.forms import formsets
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def get6(request):
    if request.method=="GET":
        recenser=Parents.objects.all()
        serializer = ParentS(recenser, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ParentS(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   

@csrf_exempt
def get_id6(request,pk):
    try:
        recenser = Parents.objects.get(pk=pk)
    except recenser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ParentS(recenser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        dataR = JSONParser().parse(request)
        serializer = ParentS(recenser, data=dataR)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recenser.delete()
        return HttpResponse(status=204)

