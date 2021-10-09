from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
