"""yeeee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

#分頁連結
from  django.contrib import admin
from django.urls import path
from mysite.views import date,index,lotto,showpost,mychart,chart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('date/', date),
    path('', index),
    path('lotto/',lotto),
    path('post/<str:slug>/',showpost),#定義post後面接的網址是字串，然後呼叫showpost
    path('mychart/',mychart),#全部顯示
    path('mychart/<int:bid>/',mychart),#顯示分店
    path('chartbydate/<int:year>/<int:month>/',chart),
    path('chartbydate/<int:year>/',chart),
]