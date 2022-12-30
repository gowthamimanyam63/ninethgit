from django.shortcuts import render

# Create your views here.
def file2(request):
    d={'name':'ratish','age':18}
    return render(request,'file2.html',context=d)