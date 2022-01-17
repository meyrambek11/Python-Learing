from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Page for shirts")


def categories(request, tshirtsID):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Staties for categories</h1><p>{tshirtsID}</p>")


def archive(request, year):
    if 2021 <= int(year) <= 3021:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Archive for year</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Page Not Found")
