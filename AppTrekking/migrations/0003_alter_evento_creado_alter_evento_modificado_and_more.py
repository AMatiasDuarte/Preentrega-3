# Generated by Django 4.1.7 on 2023-04-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrekking', '0002_alter_evento_creado_alter_evento_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='creado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='modificado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trekking',
            name='creado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trekking',
            name='modificado',
            field=models.DateTimeField(),
        ),
    ]
