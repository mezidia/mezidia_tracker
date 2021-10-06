from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]


def index(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = None
    for room_object in rooms:
        if room_object['id'] == int(pk):
            room = room_object
    context = {'room': room}
    return render(request, 'base/room.html', context)
