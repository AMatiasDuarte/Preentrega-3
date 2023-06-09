# Generated by Django 4.1.7 on 2023-04-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrekking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='creado',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='estado',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='modificado',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trekking',
            name='creado',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trekking',
            name='estado',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trekking',
            name='modificado',
            field=models.DateField(),
        ),
    ]
