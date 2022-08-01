# Generated by Django 4.0.6 on 2022-08-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_customer_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
        migrations.AddField(
            model_name='customer',
            name='Gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=6, null=True),
        ),
    ]
