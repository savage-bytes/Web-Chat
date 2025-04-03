from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.room
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    time = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    room = models.CharField(max_length=100, null=True, blank=True)  # Keep this temporarily
    
    def __str__(self):
        return f"{self.user}: {self.value[:30]}"
    
    class Meta:
        ordering = ['time']
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'
