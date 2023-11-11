from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import abouts

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj2=abouts.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj2})
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("hello how are you")
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #sub=x-y
    #mul=x*y
    #return render(request,"result.html",{'result':res,'subs':sub,'divi':div,'multi':mul})
