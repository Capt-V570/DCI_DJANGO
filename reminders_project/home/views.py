from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "home/index.html")


def hello_json(request):
    # pass a dictionary with your name
    # name: your name
    return JsonResponse({"name": "Fausto Ferrara"})
