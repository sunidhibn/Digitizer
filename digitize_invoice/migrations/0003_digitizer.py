# Generated by Django 3.1.1 on 2020-09-28 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digitize_invoice', '0002_auto_20200928_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digitizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=dict)),
                ('status', models.BooleanField(default=False)),
                ('digitized_at', models.DateTimeField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digized', to='digitize_invoice.invoice')),
            ],
        ),
    ]
