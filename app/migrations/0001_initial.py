# Generated by Django 3.0.7 on 2020-08-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Billrate', models.FloatField()),
                ('payrate', models.FloatField()),
                ('Tax', models.FloatField()),
                ('margin', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('addressl1', models.CharField(max_length=50)),
                ('addressl2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('jobtitle', models.CharField(max_length=50)),
                ('technology', models.CharField(max_length=50)),
                ('rate', models.FloatField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('trainer', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('addressl1', models.CharField(max_length=50)),
                ('addressl2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('jobtitle', models.CharField(max_length=50)),
                ('technology', models.CharField(max_length=50)),
                ('rate', models.FloatField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]