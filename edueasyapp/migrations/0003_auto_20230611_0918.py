# Generated by Django 3.2.18 on 2023-06-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edueasyapp', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=60)),
                ('Password', models.TextField()),
                ('Repassword', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]