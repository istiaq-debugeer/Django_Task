# Generated by Django 4.2.1 on 2023-05-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0009_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Websitesettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='settings/')),
                ('about_title', models.CharField(max_length=100)),
                ('about_desc', models.TextField()),
                ('website_no', models.IntegerField(default=1)),
                ('client_no', models.IntegerField(default=1)),
                ('project_no', models.CharField(max_length=100)),
                ('website_desc', models.CharField(max_length=100)),
                ('about_image', models.ImageField(upload_to='settings/')),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('linkdein', models.CharField(max_length=100)),
                ('behance', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
