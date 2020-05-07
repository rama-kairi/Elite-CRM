# Generated by Django 3.0.5 on 2020-05-07 12:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Security_Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_type', models.CharField(choices=[('DD', 'DD'), ('FDR', 'FDR'), ('BG', 'BG')], default=None, max_length=10)),
                ('cretion_date', models.DateField(default=django.utils.timezone.now, verbose_name='Creation Date')),
                ('submission_date', models.DateField(default=django.utils.timezone.now, verbose_name='Submission Date')),
                ('bank_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bank Name')),
                ('amount', models.CharField(blank=True, max_length=10, null=True, verbose_name='Amount')),
                ('validity', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Validity')),
                ('maturity_amount', models.CharField(blank=True, max_length=50, verbose_name='Maturity Amount')),
                ('support_doc', models.FileField(blank=True, null=True, upload_to='', verbose_name='Supportive Document')),
            ],
            options={
                'verbose_name': 'Security Deposit',
                'verbose_name_plural': 'Security Deposit',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_no', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation Date')),
                ('tender_number', models.CharField(max_length=500, verbose_name='Tender Number / ID')),
                ('tender_name', models.CharField(max_length=500, verbose_name='Tender Name')),
                ('tender_description', models.TextField(verbose_name='Tender Description')),
                ('tender_submission_date', models.DateField(default=django.utils.timezone.now, verbose_name='Tender Submission Date')),
                ('tender_purchase_reciept', models.FileField(upload_to='', verbose_name='Tender Purchase Reciept')),
                ('tender_confirmation_reciept', models.FileField(upload_to='', verbose_name='Tender Confirmation Reciept')),
                ('physical_submission_date', models.DateField(default=django.utils.timezone.now, verbose_name='Physical Submission Date')),
                ('tech_bid_opening_date', models.DateField(default=django.utils.timezone.now, verbose_name='Technical Bid Opening Date')),
                ('bid_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='Bid Status')),
                ('bid_price_opening_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Bid price opening date')),
                ('prize_bid', models.CharField(max_length=50, verbose_name='Bid Price')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=200, null=True, verbose_name='Project Number')),
                ('project_name', models.CharField(max_length=200, null=True, verbose_name='Project Name')),
                ('project_start_date', models.CharField(max_length=200, null=True, verbose_name='Project Start Date')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Tender')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='ProjectP1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Project Start Date')),
                ('ai_sub_date', models.DateField(default=django.utils.timezone.now, verbose_name='Agreement & Indemnity Bond Submission Date')),
                ('ai_upload', models.FileField(upload_to='', verbose_name='Agreement & Indemnity Bond Upload')),
                ('ahtsn', models.CharField(max_length=50, verbose_name='Agreement Handover to Supervisor Name')),
                ('ahts', models.DateField(default=django.utils.timezone.now, verbose_name='Agreement Handover to Supervisor Date')),
                ('asd', models.DateField(default=django.utils.timezone.now, verbose_name='Agreement Submission Date')),
                ('astdn', models.CharField(max_length=50, verbose_name='Agreement Submission to (Division Name)')),
                ('astpn', models.CharField(max_length=50, verbose_name='Agreement Submission to (Person Name)')),
                ('security_deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Security_Deposit')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Tender')),
            ],
            options={
                'verbose_name': 'Project Phase - 1',
                'verbose_name_plural': 'Project Phase - 1',
            },
        ),
        migrations.CreateModel(
            name='otherContractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contructor_name', models.CharField(max_length=200, null=True, verbose_name='Contructor Name')),
                ('contructor_location', models.CharField(max_length=200, null=True, verbose_name='Contructor Location')),
                ('contact_number', models.CharField(max_length=200, null=True, verbose_name='Contact Number')),
                ('email_address', models.EmailField(max_length=200, null=True, verbose_name='Email Address')),
                ('other_contructor_bid_amount', models.CharField(max_length=200, null=True, verbose_name='Other Contructors Bid Amount')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Tender')),
            ],
            options={
                'verbose_name': 'Other Contractors',
                'verbose_name_plural': 'Other Contractors',
            },
        ),
    ]
