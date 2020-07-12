# Generated by Django 3.0.8 on 2020-07-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20200710_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumeintro', models.CharField(blank=True, default='Optimizing problems by thinking out of the box. A learning enthusiast grasping and observing patterns in day-to-day activities. I am comfortable with a lot of tech languages & frameworks and would love to work in a very dynamic & aspirational environment. Passionate about Competitive programming, Algorithms, Data Science and Web Development. Playing badminton and Cooking being the favorite pastime.', max_length=400)),
                ('resumename', models.CharField(default='Aashu Yadav', max_length=20)),
                ('resumeaddress', models.CharField(blank=True, default='Narnaul,Haryana,India', max_length=50)),
                ('resumephone', models.CharField(blank=True, default='+919996143731', max_length=13)),
               
            ],
        ),
    ]