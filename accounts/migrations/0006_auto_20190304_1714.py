# Generated by Django 2.1.7 on 2019-03-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(blank=True, upload_to='profile_image'),
        ),
    ]