# Generated by Django 3.2.18 on 2023-06-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edueasyapp', '0007_remove_sign_repassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]