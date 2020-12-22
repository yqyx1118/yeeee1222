from django.db import models
from django.utils import timezone #時區時間

# Create your models here.

class Post(models.Model):#一個資料表
    title = models.CharField(max_length=200)#標題 限制200字 charfield欄位格式
    slug = models.CharField(max_length=200)#自訂網址 限制200字
    body = models.TextField()#內容 textfield不預設發多少字
    pub_date = models.DateTimeField(default=timezone.now)#張貼時間

    class Meta:
        ordering = ('-pub_date',)#張貼日期遞減排序(最新放最上面)

    def __str__(self):
        return self.title
    
class AccessInfo(models.Model):#一個資料表
    access_time = models.DateTimeField(default=timezone.now)#張貼時間

    class Meta:
        ordering = ('-access_time',)#張貼日期遞減排序(最新放最上面)

    def __str__(self):
        return self.access_time
    
class Branch(models.Model):#一個資料表
    title = models.CharField(max_length=200)#標題 限制200字 charfield欄位格式
    name = models.CharField(max_length=200)#自訂網址 限制200字
     
    def __str__(self):
        return self.title
    
class StoreIncome(models.Model):#一個資料表
    income_year=models.CharField(max_length=4)
    income_month=models.CharField(max_length=2)
    income = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)#一定要從branch取出
    
     
    def __str__(self):
        return str(self.income)
