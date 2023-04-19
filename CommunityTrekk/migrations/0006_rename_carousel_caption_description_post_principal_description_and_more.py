# Generated by Django 4.1.7 on 2023-04-19 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityTrekk', '0005_post_imagen2_post_imagen3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='carousel_caption_description',
            new_name='principal_description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='carousel_caption_title',
            new_name='principal_title',
        ),
        migrations.AddField(
            model_name='post',
            name='created_the',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]