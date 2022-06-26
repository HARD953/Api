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
def get9(request):
    if request.method=="GET":
        recenser=DonateurAno.objects.all()
        serializer = DanteurAS(recenser, many=True)
        print(dict(serializer.data))
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DanteurAS(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_id9(request,pk):
    try:
        recenser = DonateurAno.objects.get(pk=pk)
    except recenser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DanteurAS(recenser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        dataR = JSONParser().parse(request)
        serializer = DanteurAS(recenser, data=dataR)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recenser.delete()
        return HttpResponse(status=204)
@csrf_exempt
def doneffectuer(request):
    if request.method=="GET":
        recenser=EffectuerDonAno.objects.all()
        serializer = EffectuerDS(recenser, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EffectuerDS(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ddoneffectuer(request,pk):
    try:
        recenser = EffectuerDonAno.objects.get(pk=pk)
    except recenser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EffectuerDS(recenser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        dataR = JSONParser().parse(request)
        serializer = EffectuerDS(recenser, data=dataR)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recenser.delete()
        return HttpResponse(status=204)

