from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bye(request):
    return render(request,'app2/bye.html')
