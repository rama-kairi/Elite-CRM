# Generated by Django 3.0.5 on 2020-05-10 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0004_auto_20200510_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manpower.labourDesignation', verbose_name='Labour Designation'),
        ),
        migrations.AlterField(
            model_name='labour',
            name='skill_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manpower.labourSkillType', verbose_name='Labour Skill Type'),
        ),
    ]
