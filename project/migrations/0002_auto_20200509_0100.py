# Generated by Django 3.0.5 on 2020-05-08 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectrepeter',
            options={'verbose_name': 'Project Repeter',
                     'verbose_name_plural': 'Project Repeter'},
        ),
        migrations.AlterModelOptions(
            name='projectstart',
            options={'verbose_name': 'Project Start',
                     'verbose_name_plural': 'Project Start'},
        ),
        migrations.AlterField(
            model_name='projectrepeter',
            name='from_date',
            field=models.DateField(default='2020-04-08',
                                   verbose_name='From Date'),
        ),
        migrations.CreateModel(
            name='RaoStatus',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('project_rep', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectRepeter')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(
                    auto_now_add=True, verbose_name='Current Date & Time')),
                ('followup_by', models.CharField(max_length=200, null=True,
                                                 verbose_name='Follow Up Done By (person name)')),
                ('followup_to', models.CharField(max_length=200, null=True,
                                                 verbose_name='Follow Up Done To (person name)')),
                ('followup_remarks', models.CharField(max_length=500,
                                                      null=True, verbose_name='Follow Up Remarks')),
                ('project_rep', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectRepeter')),
            ],
        ),
    ]
