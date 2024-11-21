# Generated by Django 3.2 on 2023-07-26 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movil', '0004_endpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movil', models.BooleanField(default=True)),
                ('fijo', models.BooleanField(default=True)),
                ('orange1', models.BooleanField(default=True)),
                ('orange2', models.BooleanField(default=True)),
                ('abct', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
