# Generated by Django 3.0.5 on 2020-05-08 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Labour Name')),
                ('dateofbirth', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Birth')),
                ('image', models.FileField(upload_to='', verbose_name='Image')),
                ('mobile_number', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('alter_number', models.CharField(max_length=15, verbose_name='Alternate Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('address', models.CharField(max_length=400, verbose_name='Address')),
                ('resume', models.FileField(upload_to='Resume')),
                ('aadhar_number', models.CharField(max_length=20, verbose_name='Aadhar Number')),
                ('aadhar_photo', models.FileField(blank=True, upload_to='Aadhar_photo', verbose_name='Aadhar Card Photo')),
                ('pan_number', models.CharField(max_length=20, verbose_name='PAN Number')),
                ('pan_photo', models.FileField(upload_to='', verbose_name='PAN Card Photo')),
                ('highest_qual', models.CharField(max_length=200, verbose_name='Highest Qualifications')),
                ('highest_qual_photo', models.FileField(upload_to='', verbose_name='Proof of Highest Qualification')),
                ('ten_certi', models.FileField(upload_to='', verbose_name='10th Certificate')),
                ('twelve_certi', models.FileField(upload_to='', verbose_name='12th Certificate')),
                ('tech_certificate_name', models.CharField(max_length=300, verbose_name='Technical Certificate Name')),
                ('tech_certi', models.FileField(blank=True, upload_to='', verbose_name='Technical Certificate')),
                ('UAN_number', models.CharField(max_length=200, null=True, verbose_name='UAN Number')),
            ],
            options={
                'verbose_name': 'Labour List',
                'verbose_name_plural': 'Labour List',
            },
        ),
        migrations.CreateModel(
            name='SuperVisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('re_password', models.CharField(max_length=50, verbose_name='Confirm Password')),
                ('name', models.CharField(max_length=250, verbose_name='Supervisor Name')),
                ('dateofbirth', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Birth')),
                ('image', models.FileField(upload_to='', verbose_name='Profile Picture')),
                ('mobile_number', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('alter_number', models.CharField(max_length=15, verbose_name='Alternate Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('address', models.CharField(max_length=500, verbose_name='Supervisor Address')),
                ('resume', models.FileField(upload_to='', verbose_name='Upload Supervisor Resume')),
                ('aadhar_number', models.CharField(max_length=20, verbose_name='Aadhar Number')),
                ('aadhar_photo', models.FileField(upload_to='', verbose_name='Aadhar Card Scan Copy')),
                ('pan_number', models.CharField(max_length=20, verbose_name='PAN Card Number')),
                ('pan_photo', models.FileField(upload_to='', verbose_name='PAN Card Scan Copy')),
                ('highest_qual', models.CharField(max_length=200, verbose_name='Highest Qualifications')),
                ('highest_qual_photo', models.FileField(upload_to='', verbose_name='Proof of Highest Qualification')),
                ('ten_certi', models.FileField(upload_to='', verbose_name='10th Certificate')),
                ('twelve_certi', models.FileField(upload_to='', verbose_name='12th Certificate')),
                ('tech_certificate_name', models.CharField(max_length=300, verbose_name='Technical Certificate Name')),
                ('tech_certi', models.FileField(upload_to='', verbose_name='Technical Certificate')),
                ('UAN_number', models.CharField(max_length=200, verbose_name='UAN Number')),
                ('is_employee', models.BooleanField(verbose_name='Is Supervisor is Employee of Elite Works')),
            ],
            options={
                'verbose_name': 'Supervisors List',
                'verbose_name_plural': 'Supervisors List',
            },
        ),
    ]
