from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SMTPAccount, EmailRecipient
from unfold.admin import ModelAdmin
# Register your models here.

class SMTPAccountAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('email_address', 'smtp_server', 'smtp_port', 'username', 'proxy_address', 'proxy_port', 'last_sent_at', 'total_sent_count', 'daily_sent_count', 'smtp_banned' ,'created_at')
    search_fields = ('email_address', 'smtp_server', 'username', 'proxy_address')
    list_filter = ('smtp_server', 'last_sent_at', 'created_at')

class EmailRecipientAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'custom_link', 'phone', 'extra_field1', 'extra_field2', 'extra_field3', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'extra_field1', 'extra_field2', 'extra_field3')
    list_filter = ('created_at',)

admin.site.register(SMTPAccount, SMTPAccountAdmin)
admin.site.register(EmailRecipient, EmailRecipientAdmin)