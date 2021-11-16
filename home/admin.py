from django.contrib import admin
from .models import ContactMessage, Setting, SubscribedUser, MailMessage
# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)

class SubscribedUserAdmin(admin.ModelAdmin):
     list_display = ['email', 'date']

admin.site.register(SubscribedUser, SubscribedUserAdmin)

class MailMessageAdmin(admin.ModelAdmin):
     list_display = ['subject','send_it']

admin.site.register(MailMessage, MailMessageAdmin)