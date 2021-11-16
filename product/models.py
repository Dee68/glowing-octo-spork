from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True','True'),
        ('False','False'),
    )
    # id = models.AutoField(unique=True)
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', blank=True,null=True, on_delete=models.CASCADE, related_name='children')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(null=False,unique=True)
    image = models.ImageField(blank=True, upload_to='categories/%Y/%m/%d/')
    status = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"
            
    def get_absolute_url(self):
        return reverse('products:category_products', args=[self.slug])   


    class Meta:
        verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True, upload_to='products/')
    status = models.CharField(max_length=5, choices=STATUS)
    available = models.BooleanField(default=True)
    details = RichTextUploadingField()#models.TextField()
    specification = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField()
    miniamount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"

    def get_absolute_url(self):
        return reverse('products:product_details',args=[self.id,self.slug])   

    def __str__(self):
        return self.title

class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to='pictures/')
    # status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    GENDER = (
        ('male','male'),
        ('female','female'),
    )
    TITLE = (
        ('mr.','mr.'),
        ('mrs.','mrs.'),
        ('ms.','ms.'),
        ('dr.','dr.'),
        ('prof.', 'prof.'),
        ('king','king'),
        ('chief','chief'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    title = models.CharField(max_length=5, choices=TITLE)
    wishlist = models.ManyToManyField(Product,blank=True)
    # device = models.CharField(max_length=200,null=True, blank=True)
    

    def __str__(self):
        name = self.user.username
        return str(name)
        

class Cart(models.Model):
    customer =models.ForeignKey(User,on_delete = models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True,null=True)
    update_at = models.DateTimeField(auto_now=True,null=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    cart_id = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    complete = models.BooleanField(default=False,null=True,blank=True)
    invoice_id = models.CharField(max_length=100,null=True)# invoice id

    # @property
    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.get_total for item in orderitems])
    #     return total

    # @property
    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.quantity for item in orderitems])
    #     return total

    def __str__(self) :
        return  "Order of {} on {}".format(str(self.id),str(self.date_ordered))



class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=150,null=False)
    city = models.CharField(max_length=150,null=False)
    state = models.CharField(max_length=150,null=False)
    zipcode = models.CharField(max_length=150,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Notification(models.Model):
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = RichTextField()
    read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Notification for: self.recipient.user"
