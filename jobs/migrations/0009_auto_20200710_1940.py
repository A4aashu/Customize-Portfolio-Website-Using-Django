# Generated by Django 3.0.8 on 2020-07-10 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20200710_1939'),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name='about',
            name='phone',
        ),
    ]