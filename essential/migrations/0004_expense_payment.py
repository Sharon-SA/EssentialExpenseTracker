# Generated by Django 4.0.2 on 2022-05-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0003_remove_report_net_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='payment',
            field=models.CharField(choices=[('CH', 'Cash'), ('CR', 'Credit'), ('DB', 'Debit')], default='CH', max_length=2),
        ),
    ]
