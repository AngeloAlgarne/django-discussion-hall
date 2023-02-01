from django.shortcuts import render, redirect
from django.db.models import Q
from . import models
from . import forms

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = models.Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) | 
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    
    topics = models.Topic.objects.all()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
    }
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
