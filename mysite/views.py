
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from mysite.models import Post,AccessInfo,Branch,StoreIncome
import random
from  datetime import  datetime  

def index(request):
    rec=AccessInfo() #產生新的紀錄
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts=Post.objects.all()#到資料庫撈資料，打包給posts
    name = "YEE"
    now=datetime.now()
    return render(request,'index.html',locals()) #來自於瀏覽器的請求,要渲染的檔案,記憶體的變數資料 #是為了index裡的{{}}(模板)
def date(request):

    return JsonResponse({'date':datetime.datetime.now()})
def showpost(request,slug):
    now=datetime.now()

    try:
        post=Post.objects.get(slug=slug)
        return render(request,"post.html",locals())
    except :
        return redirect("/")
    
def mychart(request,bid=0):
    now=datetime.now()
    #data=StoreIncome.objects.all() all撈全部的資料 get只撈一筆資料(要很肯定有這筆資料) filter撈符合條件的資料
    branches = Branch.objects.all()   
    if  bid == 0:
        data = StoreIncome.objects.all()
    else:
        data =StoreIncome.objects.filter(branch=bid)
    title : "各分店營收情形"
    return render(request,"mychart.html",locals())


def chart(request,year=0,month=0):
    now=datetime.now()
    branches = Branch.objects.all()   
    if  year == 0 :
        data = StoreIncome.objects.all()
    else:
        data =StoreIncome.objects.filter(income_year=year)
        if month >0:
            data = data.filter(income_month=month)
            
    if year>0 and  month>0 :
        title = "{}年{}月各分店營收情形".format(year,month)
    elif year>0:
        title = "{}年各分店營收情形".format(year)
    else:
        title = "各分店營收情形"
    return render(request,"mychart.html",locals())

    

def  lotto(request):
    
    lottos=list()
    lucky=random.randint(1,42)
    for i in range(5):
        lottos.append(random.randint(1,42))
    
    return render(request,'lotto.html',locals())

