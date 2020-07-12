# Generated by Django 3.0.8 on 2020-07-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0025_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Educational website', max_length=20)),
                ('projectphoto', models.ImageField(blank=True, upload_to='images/')),
                ('projectlink', models.URLField(blank=True, default='https://a4aashu.github.io/educational-website/')),
            ],
        ),
    ]