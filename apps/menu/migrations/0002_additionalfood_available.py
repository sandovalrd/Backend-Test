# Generated by Django 2.0.1 on 2018-01-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalfood',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
