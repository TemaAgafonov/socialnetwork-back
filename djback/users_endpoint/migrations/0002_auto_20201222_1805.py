# Generated by Django 3.1.4 on 2020-12-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='users_endpoint.user'),
        ),
    ]
