# Generated by Django 4.0.10 on 2023-02-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Islam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Psychology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sciences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]