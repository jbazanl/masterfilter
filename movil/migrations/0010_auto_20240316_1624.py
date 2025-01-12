# Generated by Django 3.2 on 2024-03-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movil', '0009_endpoint_wsp'),
    ]

    operations = [
        migrations.AddField(
            model_name='permision',
            name='amarilla',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='permision',
            name='infobel',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='permision',
            name='fijo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permision',
            name='movil',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permision',
            name='orange1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permision',
            name='orange2',
            field=models.BooleanField(default=False),
        ),
    ]
