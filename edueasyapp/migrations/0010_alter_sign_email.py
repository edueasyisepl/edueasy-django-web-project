# Generated by Django 3.2.18 on 2023-06-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edueasyapp', '0009_alter_sign_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
