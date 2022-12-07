from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):

    # create a range of numbers (0 to 2000)
    numbers = range(0 + 1, 2001)

    # template context "variables"
    context = {"numbers": numbers}

    return render(request, "home/index.html", context)


def hello_json(request):
    return JsonResponse({"name": "Fausto Ferrara"})
