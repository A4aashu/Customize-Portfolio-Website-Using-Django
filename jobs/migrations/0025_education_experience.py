# Generated by Django 3.0.8 on 2020-07-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_auto_20200710_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default='Bachelor of Technology', max_length=100)),
                ('field', models.CharField(default='Computer science', max_length=100)),
                ('date', models.CharField(default='2017-2021', max_length=10)),
                ('nameoforg', models.CharField(default='Kiit University ,Bhubaneswar', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workas', models.CharField(blank=True, default='Full stack developer', max_length=100)),
                ('date', models.CharField(blank=True, default='May(2019)-July(2019)', max_length=100)),
                ('nameoforg', models.CharField(blank=True, default='Tekserve ,Egypt', max_length=100)),
                ('expintro', models.CharField(blank=True, default='Made an english learning website front end and made app similar to uber eats with help of React Native,Html,Css and Javascript.', max_length=500)),
            ],
        ),
    ]
