from django.db import models
from django.utils import timezone

class SMTPAccount(models.Model):
    email_address = models.EmailField(max_length=255, unique=True)
    smtp_server = models.CharField(max_length=255)
    smtp_port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # You can encrypt this later
    proxy_address = models.CharField(max_length=255, null=True, blank=True)
    proxy_port = models.IntegerField(null=True, blank=True)
    last_sent_at = models.DateTimeField(null=True, blank=True)
    total_sent_count = models.IntegerField(default=0)
    daily_sent_count = models.IntegerField(default=0)
    smtp_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email_address


class EmailRecipient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    custom_link = models.URLField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    extra_field1 = models.CharField(max_length=255, null=True, blank=True)
    extra_field2 = models.CharField(max_length=255, null=True, blank=True)
    extra_field3 = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email