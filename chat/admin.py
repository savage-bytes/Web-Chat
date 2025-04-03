from django.contrib import admin
from chat.models import Room, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('time',)
    fields = ('user', 'value', 'time')
    ordering = ('-time',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'created_at', 'message_count')
    search_fields = ('room',)
    inlines = [MessageInline]
    
    def message_count(self, obj):
        return obj.messages.count()
    
    message_count.short_description = 'Messages'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('short_value', 'user', 'get_room', 'time')
    list_filter = ('room_id__room', 'user', 'time')
    search_fields = ('value', 'user', 'room_id__room')
    readonly_fields = ('time',)
    date_hierarchy = 'time'
    
    def short_value(self, obj):
        return obj.value[:50] + '...' if len(obj.value) > 50 else obj.value
    
    def get_room(self, obj):
        return obj.room_id.room
    
    short_value.short_description = 'Message'
    get_room.short_description = 'Room'
