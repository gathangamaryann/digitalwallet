# Generated by Django 4.0.6 on 2022-08-01 18:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_remove_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='origin_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_origin_account', to='wallet.account'),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='card',
            name='issued_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='currency',
            name='amount',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='transaction_amount',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user_id',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='reward',
            name='customer_id',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='third_party',
            name='amount',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='amount',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='history',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user_id',
            field=models.PositiveBigIntegerField(),
        ),
    ]
