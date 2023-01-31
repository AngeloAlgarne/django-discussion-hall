from django.shortcuts import render
from . import models

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Room1'},
#     {'id': 2, 'name': 'Room2'},
#     {'id': 3, 'name': 'Room3'},
# ]


def home(request):
    rooms = models.Room.objects.all()
    context = {'rooms': rooms}
    return render(
        request=request,
        template_name='base/home.html',
        context=context,
    )


def room(request, pk):
    room = models.Room.objects.get(id=pk)
    discussions = models.Discussion.objects.all().filter(room=room)
    context = {'room': room, 'discussions': discussions}
    return render(
        request=request,
        template_name='base/room.html',
        context=context,
    )
