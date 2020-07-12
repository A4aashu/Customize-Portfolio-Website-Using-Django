# Generated by Django 3.0.8 on 2020-07-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=20)),
                ('profilephoto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('facebook', models.URLField(blank=True, default='#')),
                ('insta', models.URLField(blank=True, default='#')),
                ('skype', models.URLField(blank=True, default='#')),
                ('linkedin', models.URLField(blank=True, default='#')),
                ('github', models.URLField(blank=True, default='#')),
                ('hero', models.CharField(default='abc', max_length=20)),
                ('skill1', models.CharField(default='abc', max_length=20)),
                ('skill2', models.CharField(blank=True, default='abc', max_length=20)),
                ('skill3', models.CharField(blank=True, default='abc', max_length=20)),
                ('skill4', models.CharField(blank=True, default='abc', max_length=20)),
                ('skill5', models.CharField(blank=True, default='abc', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.RemoveField(
            model_name='job',
            name='summary',
        ),
        migrations.AddField(
            model_name='job',
            name='percent',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='job',
            name='skill',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
