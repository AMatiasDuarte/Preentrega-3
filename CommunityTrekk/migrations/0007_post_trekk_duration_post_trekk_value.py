# Generated by Django 4.1.7 on 2023-04-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityTrekk', '0006_rename_carousel_caption_description_post_principal_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trekk_duration',
            field=models.CharField(default='1 día', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='trekk_value',
            field=models.CharField(default='$0', max_length=10),
        ),
    ]
