from django.shortcuts import render

from django.http import JsonResponse

def ism_qaytaradigan(request):
    data ={
        "id": 1,
        "value": "Bexruz",
        "status":"IT programmist",
        "description":"birinchi funksiyadan qaytgan qiymat"
    }
    return JsonResponse(data)
def ism_qaytaradigan2(request):
    date ={
        "id":2,
        "value":"Shuxrat",
        "status":"bugalter",
        "description": "birinchi funksiyadan qaytgan qiymat"
    }
    return JsonResponse(date)
def ism_qaytaradigan3(request):
    date ={
        "id":3,
        "value": "Abbos",
        "status": "Novvoy",
        "description": "birinchi funksiyadan qaytgan qiymat"

    }
    return JsonResponse(date)

