# Generated by Django 5.1.3 on 2024-12-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectify', '0009_alter_profile_bio_alter_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]