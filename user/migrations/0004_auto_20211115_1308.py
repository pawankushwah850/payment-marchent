# Generated by Django 3.2.9 on 2021-11-15 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='user.kycdocuments'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registered_bank',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='user.bankregistered'),
        ),
    ]
