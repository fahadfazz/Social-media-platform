# Generated by Django 5.1.3 on 2024-12-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectify', '0005_alter_profile_bio_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]