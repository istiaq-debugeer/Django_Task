# Generated by Django 4.2.1 on 2023-05-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0006_featureplans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
