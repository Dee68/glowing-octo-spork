# Generated by Django 3.2.9 on 2021-12-02 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211201_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailmessage',
            name='attachement',
        ),
    ]
