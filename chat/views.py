from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from collections import defaultdict

# Simple in-memory store for room participants (in a production app, use Redis or a database)
room_participants = defaultdict(set)

# Create your views here.

def index(request):
    return render(request,'index.html')

def room(request, room):
    username = request.GET.get('username')
    
    # Add user to room participants if username is provided
    if username:
        room_participants[room].add(username)
    
    # Get or create the room
    room_obj, created = Room.objects.get_or_create(room=room)
    
    return render(request, 'chatroom.html', {
        'room': room,
        'username': username
    })

def checkview(request):
    room = request.POST['roomid']
    username = request.POST['username']

    if Room.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(room=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    # Get the room object
    room_obj = get_object_or_404(Room, room=room_id)
    
    # Create the message
    new_message = Message.objects.create(
        value=message, 
        user=username, 
        room_id=room_obj
    )
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    # Get the room object
    room_obj = get_object_or_404(Room, room=room)
    
    # Get messages for this room
    messages = Message.objects.filter(room_id=room_obj)
    
    # Format messages for JSON
    message_list = []
    for message in messages:
        message_list.append({
            'value': message.value,
            'user': message.user,
            'time': message.time.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return JsonResponse({"messages": message_list})

def getParticipants(request, room):
    participants = list(room_participants[room])
    return JsonResponse({"participants": participants})
    
