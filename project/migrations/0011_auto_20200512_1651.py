# Generated by Django 3.0.5 on 2020-05-12 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_projectrepeter_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrepeter',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='From Date'),
        ),
    ]
