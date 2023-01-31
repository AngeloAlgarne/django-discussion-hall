from django.shortcuts import render, redirect
from . import models
from . import forms

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
    context = {
        'room': room,
        'discussions': discussions
    }
    return render(
        request=request,
        template_name='base/room.html',
        context=context,
    )


def createRoom(request):
    form = forms.RoomForm()

    if request.method == 'POST':
        form = forms.RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(
        request=request,
        template_name='base/room_form.html',
        context=context,
    )


def editRoom(request, pk):
    room = models.Room.objects.get(id=pk)
    form = forms.RoomForm(instance=room)
    
    if request.method == 'POST':
        form = forms.RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(
        request=request,
        template_name='base/room_form.html',
        context=context,
    )

def deleteRoom(request, pk):
    room = models.Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'object': room}
    return render(
        request=request,
        template_name='base/delete.html',
        context=context,
    )