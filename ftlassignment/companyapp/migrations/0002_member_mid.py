# Generated by Django 2.2.7 on 2020-09-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mid',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]