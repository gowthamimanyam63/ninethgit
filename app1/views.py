from django.shortcuts import render

# Create your views here.
def file1(request):
    d={'name':'gowthami'}
    return render(request,'file1.html',context=d)