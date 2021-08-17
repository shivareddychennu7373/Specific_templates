from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return render(request,'app1/hai.html')