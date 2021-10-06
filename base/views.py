from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'base/home.html')


def room(request):
    return render(request, 'base/room.html')
