# Generated by Django 3.2.9 on 2021-12-04 14:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20211118_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
