# Generated by Django 3.1.4 on 2020-12-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('followed', models.BooleanField()),
                ('photo', models.URLField()),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
        ),
    ]
