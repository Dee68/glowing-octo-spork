from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

# Create your models here.
class Service(models.Model):
    ICON_STATUS = (
        ('calendar','calendar'),
        ('clapperboard','clapperboard'),
        ('drive','drive'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    description = RichTextUploadingField()
    available = models.BooleanField(default=True)
    image = models.ImageField(blank=True,upload_to="services/")
    contract = RichTextUploadingField(blank=True, null=True)
    icon_status = models.CharField(max_length=20,choices=ICON_STATUS, default='calendar')


    def __str__(self):
        return self.title


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"