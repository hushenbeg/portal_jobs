# Generated by Django 2.1.4 on 2019-02-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BangaloreJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_date', models.DateField()),
                ('job_title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('eligibility', models.CharField(max_length=64)),
                ('last_date', models.DateField()),
                ('more_information', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ChennaiJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_date', models.DateField()),
                ('job_title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('eligibility', models.CharField(max_length=64)),
                ('last_date', models.DateField()),
                ('more_information', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='HydJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_date', models.DateField()),
                ('job_title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('eligibility', models.CharField(max_length=64)),
                ('last_date', models.DateField()),
                ('more_information', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PuneJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_date', models.DateField()),
                ('job_title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('eligibility', models.CharField(max_length=64)),
                ('last_date', models.DateField()),
                ('more_information', models.CharField(max_length=64)),
            ],
        ),
    ]
