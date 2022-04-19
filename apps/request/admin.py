from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'frase_enviada', 'user', 'response', 'response_status', 'conversation_id', 'algorithm', 'site_id', 'bot_name')

admin.site.register(Request, RequestAdmin)
