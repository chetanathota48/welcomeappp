from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    res = HttpResponse("""<html><body bgcolor=cyan><center><h1>welcome to lokiesh it>
    </h1></center></body></html>""")
    return res
