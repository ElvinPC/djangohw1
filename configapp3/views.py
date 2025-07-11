from django.shortcuts import render

from django.http import JsonResponse

def tel_raqam(request):
    data ={
        "ism":"Dilmurod",
        "Tel raqam":"+998998009080"
    }
    return JsonResponse(data)


def tel_raqam2(request):
    data ={
        "ism":"Jaxongir",
        "Tel raqam":"+998901231234"

    }
    return JsonResponse(data)

def tel_raqam3(request):
    data ={
        "ism":"Abdulloh",
        "Tel raqam":"+998509784567"
    }

    return JsonResponse(data)