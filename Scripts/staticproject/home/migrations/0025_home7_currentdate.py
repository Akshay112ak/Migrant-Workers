# Generated by Django 4.2.2 on 2023-08-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_home1_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='home7',
            name='CURRENTDATE',
            field=models.DateField(null=True),
        ),
    ]
