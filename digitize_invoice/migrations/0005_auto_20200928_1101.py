# Generated by Django 3.1.1 on 2020-09-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitize_invoice', '0004_auto_20200928_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitizer',
            name='data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='digitizer',
            name='digitized_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
