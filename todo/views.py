from django.shortcuts import redirect, render,HttpResponse
from django import forms
from django.forms import widgets
from .models import Todolist
# Create your views here.
class RegForm(forms.Form):
    thing= forms.CharField(required=True,error_messages={
        "required":"待办清单不能为空",
    })
    level= forms.IntegerField(max_value=99,min_value=1,required=True,error_messages={
        "max_value":"最大值99",
        "min_value":"最小值1",
        "required":"优先级不能为空",})

class Reg_Form(forms.Form):
    level= forms.IntegerField(max_value=99,min_value=1,required=True,error_messages={
        "max_value":"最大值99",
        "min_value":"最小值1",
        "required":"优先级不能为空",})

def home(request):
    if request.method =="POST":
        thing=request.POST.get("thing")
        level=request.POST.get("level")
        obj = RegForm(request.POST)
        if obj.is_valid():
            a_row=Todolist(thing=thing,done=False,level=level,details=" ")
            a_row.save()
            content={"清单":Todolist.objects.all().order_by('done','-level'),"信息":"添加成功"}
            return render(request,"home.html",content)
        else:
            content={"清单":Todolist.objects.all().order_by('done','-level'),"警告":"添加失败"}
            return render(request,"home.html",content)

    elif request.method =="GET":
        content={"清单":Todolist.objects.all().order_by('done','-level')}
        return render(request,"home.html",content)
        
def about(request):

    return render(request,"about.html")

def edit(request,i_id):
    if request.method=="POST":
        if request.POST["已修改事项"]=="":
            return render(request,"edit.html",{"警告":"请输入内容！"})
        else:
            a=Todolist.objects.get(id=i_id)
            a.thing=request.POST["已修改事项"]
            a.save()
            return redirect("todo:主页")
    elif request.method=="GET":
        content={'待修改事项': Todolist.objects.get(id=i_id).thing}
        return render(request,"edit.html",content)

def details(request,i_id):
    if request.method=="POST":
        g=request.POST.get("已修改详细内容")
        a=Todolist.objects.get(id=i_id)
        a.details=g
        a.save()
        return redirect("todo:主页")

    elif request.method=="GET":
        content={'待修改详细内容': Todolist.objects.get(id=i_id).details}
        return render(request,"details.html",content)


def edit_level(request,i_id):

    if request.method=="POST":
        level=request.POST.get("level")
        obj = Reg_Form(request.POST)
        if obj.is_valid():
            a=Todolist.objects.get(id=i_id)
            a.level=level
            a.save()
            return redirect("todo:主页")
        else:
            return render(request,"edit_level.html",{"警告":"请输入内容！"})

    elif request.method=="GET":
        content={'level': Todolist.objects.get(id=i_id).level}
        return render(request,"edit_level.html",content)

def delete(request,i_id):
    a=Todolist.objects.get(id=int(i_id))
    a.delete()
    return redirect("todo:主页")
    
def cross(request,i_id):
    if request.POST["完成状态"]=="已完成":
        a=Todolist.objects.get(id=i_id)
        a.done=True
        a.save()
        return redirect("todo:主页")
    elif request.POST["完成状态"]=="未完成":
        a=Todolist.objects.get(id=i_id)
        a.done=False
        a.save()    
        return redirect("todo:主页")
