from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class UserProfile(models.Model):
    GENDER = (
        ('male','male'),
        ('female','female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    bio = models.TextField(blank=True,null=True)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    occupation = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(blank=True, max_length=20)
    company = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(blank=True, upload_to="profile_pics/", default="/userimage.png")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def user_names(self):
        return self.user.first_name +''+self.user.last_name +'[' +self.user.username +']'

    def __str__(self):
        return str(self.user.username)


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"
    image_tag.short_description = 'Image' 
        