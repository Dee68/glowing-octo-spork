# Generated by Django 3.2.9 on 2021-12-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='/userimage.png', upload_to='profile_pics/'),
        ),
    ]