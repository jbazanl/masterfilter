# Generated by Django 3.2 on 2023-07-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movil', '0003_document_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movil', models.CharField(max_length=150)),
                ('fijo', models.CharField(max_length=150)),
                ('orange1', models.CharField(max_length=150)),
                ('orange2', models.CharField(max_length=150)),
                ('abct', models.CharField(max_length=150)),
            ],
        ),
    ]
