from django.contrib import admin
from .models import ContactMessage, Setting, SubscribedUser, MailMessage
# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(SubscribedUser),
admin.site.register(MailMessage)