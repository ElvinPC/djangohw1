from django.shortcuts import render

from django.http import JsonResponse


def hisoblash(request):
    data = {
        "amal": "5 + 3",
        "javob": 5 + 3
    }
    return JsonResponse(hisoblash)


def hisoblash2(request):
    data = {
        "amal": "34*34",
        "javob": 34 * 34
    }
    return JsonResponse(data)
def hisoblash3(request):
    data = {
        "amal": "100/100",
        "javob": 100/100
    }
    return JsonResponse(data)


