"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from configapp.views import ism_qaytaradigan
from configapp.views import ism_qaytaradigan2
from configapp.views import ism_qaytaradigan3
from configapp2.views import hisoblash
from configapp2.views import hisoblash2
from configapp2.views import hisoblash3
from configapp3.views import tel_raqam
from configapp3.views import tel_raqam2
from configapp3.views import tel_raqam3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ism/', ism_qaytaradigan),
    path('ism2/', ism_qaytaradigan2),
    path('ism3/',ism_qaytaradigan3),
    path('amallar/',hisoblash),
    path('amallar2/',hisoblash2),
    path('amallar3/',hisoblash3),
    path('malumotlar/',tel_raqam),
    path('malumotlar2/',tel_raqam2),
    path('malumotlar3/',tel_raqam3)
]
