# Generated by Django 3.2.8 on 2021-10-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=255)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('note', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('New', 'New'), ('Closed', 'Closed'), ('Read', 'Read')], default='New', max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='icons/')),
                ('facebook', models.CharField(blank=True, max_length=20)),
                ('instagram', models.CharField(blank=True, max_length=20)),
                ('twitter', models.CharField(blank=True, max_length=20)),
                ('smtpserver', models.CharField(blank=True, max_length=20)),
                ('smtpemail', models.CharField(blank=True, max_length=20)),
                ('smtppassword', models.CharField(blank=True, max_length=20)),
                ('smtpport', models.CharField(blank=True, max_length=20)),
                ('aboutus', models.TextField()),
                ('contact', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
