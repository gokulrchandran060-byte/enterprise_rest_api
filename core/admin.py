from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
