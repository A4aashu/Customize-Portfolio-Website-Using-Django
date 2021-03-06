# Generated by Django 3.0.8 on 2020-07-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_profile_backgroundimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='backgroundimage',
            field=models.ImageField(blank=True, default='images/hero-bg.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, default='https://www.facebook.com/aashu.yadav.589/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, default='https://github.com/A4aashu'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hero',
            field=models.CharField(default='Aashu Yadav', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta',
            field=models.URLField(blank=True, default='https://www.instagram.com/a4_aashu/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, default='https://www.linkedin.com/in/aashu-yadav-9000a1b4/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Aashu Yadav', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilephoto',
            field=models.ImageField(blank=True, default='images/profile_fF942u6.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill1',
            field=models.CharField(default='Designer', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill2',
            field=models.CharField(blank=True, default='Data scientist', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill3',
            field=models.CharField(blank=True, default='Free lancer', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill4',
            field=models.CharField(blank=True, default='Full stack developer', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill5',
            field=models.CharField(blank=True, default='Cool', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skype',
            field=models.URLField(blank=True, default='https://join.skype.com/invite/UJB1tZr05vWv'),
        ),
    ]
