from django.contrib import admin

# Register your models here.
from mailsender.models import Client, Mailing, Message, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname',)
    list_filter = ('email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('frequency', 'status', 'client',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'mailing',)
    list_filter = ('title',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('message', 'status',)
