# Generated by Django 3.0.7 on 2020-08-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200804_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial',
            name='margin',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
