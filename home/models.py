from django.db import models
from django.http import request
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from ckeditor_uploader.fields import RichTextUploadingField
# from .forms import MailMessageForm
from django_pandas.io import read_frame
import uuid
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    fax = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='icons/')
    facebook = models.CharField(blank=True, max_length=20)
    instagram = models.CharField(blank=True, max_length=20)
    twitter = models.CharField(blank=True, max_length=20)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=20)
    aboutus = RichTextUploadingField()#models.TextField()
    contact = RichTextUploadingField()#models.TextField()
    #references = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
        STATUS = (
            ('New','New'),
            ('Closed','Closed'),
            ('Read','Read'),
        )
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100)
        subject = models.CharField(max_length=150)
        message = models.TextField(max_length=255)
        ip = models.CharField(blank=True, max_length=50)
        note = models.CharField(blank=True, max_length=50)
        status = models.CharField(max_length=6, choices=STATUS, default='New')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name+" - message"

class SubscribedUser(models.Model):
    email = models.EmailField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.email


class MailMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=100,default='Thanking you')
    message = models.TextField()
    # attachement = models.FileField(blank=True, null=True)
    # subscribers = models.ManyToManyField(SubscribedUser)
    send_it = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        subscribers = SubscribedUser.objects.all()
        datasets = read_frame(subscribers, fieldnames=['email'])
        subscribers_list = datasets['email'].values.tolist()
        
        
        if self.send_it == True:
            # then send message
            send_mail(
            str(self.subject),
            str(self.message),
            settings.EMAIL_HOST_USER,
            subscribers_list,
            fail_silently=False
            )
            # create obj & save it
            # msg = MailMessage(subject=self.subject,
            # message=self.message,
            # send_it=self.send_it)
            # msg.save()
            # msg= MailMessage.objects.create(
            #     subject=self.subject,
            #     message=self.message,
            #     send_it=self.send_it)

       
            
    def __str__(self):
        return self.subject


    