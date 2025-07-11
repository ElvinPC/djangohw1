from django.shortcuts import render

from django.http import HttpResponse

def tel_raqam(request):
    data ={
        "ism":"Dilmurod",
        "Tel raqam":"+998998009080"
    }
    return HttpResponse(tel_raqam)


def tel_raqam2(request):
    data ={
        "ism":"Jaxongir",
        "Tel raqam":"+998901231234"

    }
    return HttpResponse(tel_raqam2)

def tel_raqam3(request):
    data ={
        "ism":"Abdulloh",
        "Tel raqam":"+998509784567"
    }

    return HttpResponse(tel_raqam3)