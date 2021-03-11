# Generated by Django 3.1.7 on 2021-03-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20210309_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='parent_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Country Parent Code'),
        ),
        migrations.AlterField(
            model_name='location',
            name='parent_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Location Parent Code'),
        ),
    ]