from mptt.admin import DraggableMPTTAdmin
from .models import Cart, Category, Product, Picture,ShippingAddress, Customer, Order
from django.contrib import admin

# Register your models here.
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count','image_tag')
    list_display_links = ('indented_title',)
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','available', 'price','category']
    list_filter = ['available','created_at','updated_at']
    list_editable = ['price','available']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Picture)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(Product, ProductAdmin)

