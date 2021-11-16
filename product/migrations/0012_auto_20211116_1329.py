# Generated by Django 3.2.9 on 2021-11-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, to='product.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('SELF', 'self'), ('DELIVERY', 'delivery')], default='DELIVERY', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('in-progress', 'in-progress'), ('is-ready', 'is-ready'), ('completed', 'completed')], default='new', max_length=50),
        ),
    ]
