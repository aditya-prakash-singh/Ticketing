# Generated by Django 4.2 on 2023-04-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='dat',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
    ]
