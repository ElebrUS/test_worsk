# Generated by Django 3.1.7 on 2021-03-10 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210310_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Add'),
        ),
    ]
