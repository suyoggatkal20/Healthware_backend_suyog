# Generated by Django 3.2 on 2021-05-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210509_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='practice_started',
            field=models.DateField(null=True),
        ),
    ]
