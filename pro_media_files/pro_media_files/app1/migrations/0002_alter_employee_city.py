# Generated by Django 4.0.5 on 2022-06-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=20),
        ),
    ]