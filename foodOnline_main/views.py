from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # print("hello")
    return render(request, 'index.html')