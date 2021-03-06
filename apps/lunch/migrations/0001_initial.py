# Generated by Django 2.0.1 on 2018-01-24 00:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_food', models.BooleanField(default=False, verbose_name='Comida Extra')),
                ('date_lunch', models.DateField(auto_now_add=True)),
                ('specification', models.CharField(blank=True, max_length=50)),
                ('additional_id', models.ForeignKey(blank=True, null=True, on_delete=False, to='menu.AdditionalFood')),
                ('employee_id', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL)),
                ('food_id', models.ForeignKey(on_delete=False, to='menu.Food')),
                ('menu_id', models.ForeignKey(on_delete=False, to='menu.Menu')),
            ],
            options={
                'verbose_name': 'Almuerzo',
            },
        ),
    ]
