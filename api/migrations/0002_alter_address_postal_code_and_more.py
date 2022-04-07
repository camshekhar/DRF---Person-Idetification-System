# Generated by Django 4.0.3 on 2022-04-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='acc_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='yop',
            field=models.CharField(max_length=25, null=True),
        ),
    ]