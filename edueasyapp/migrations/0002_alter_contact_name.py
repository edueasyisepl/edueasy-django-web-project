# Generated by Django 3.2.18 on 2023-06-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edueasyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
