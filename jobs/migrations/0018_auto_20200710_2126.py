# Generated by Django 3.0.8 on 2020-07-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20200710_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='aboutphoto',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='intro',
            field=models.CharField(blank=True, default=' I’ve gained some practical knowledge in the field of Computer Programming. Therefore, I am looking for an opportunity where I can utilize my skills, put my learning into practice and make a contribution in the field of Computing and Technology. ', max_length=500),
        ),
    ]
