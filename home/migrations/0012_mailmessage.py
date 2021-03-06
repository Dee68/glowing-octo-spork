# Generated by Django 3.2.9 on 2021-12-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_mailmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Thanking you', max_length=100)),
                ('message', models.TextField()),
                ('send_it', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
