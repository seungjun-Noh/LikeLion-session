# Generated by Django 4.0.3 on 2022-04-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='blog',
            name='email',
            field=models.EmailField(max_length=128),
        ),
    ]
