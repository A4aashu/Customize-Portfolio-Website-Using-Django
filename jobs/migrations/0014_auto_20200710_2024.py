# Generated by Django 3.0.8 on 2020-07-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20200710_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='backgroundimage',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilephoto',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill5',
            field=models.CharField(blank=True, default='Cool😎', max_length=20),
        ),
    ]
