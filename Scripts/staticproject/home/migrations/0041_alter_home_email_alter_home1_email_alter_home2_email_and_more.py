# Generated by Django 4.2.2 on 2023-09-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_remove_home1_file_home18'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='home1',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='home2',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='home3',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
