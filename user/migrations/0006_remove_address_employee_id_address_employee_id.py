# Generated by Django 4.0.1 on 2022-03-08 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_address_employee_id_address_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='employee_id',
        ),
        migrations.AddField(
            model_name='address',
            name='employee_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.employee'),
            preserve_default=False,
        ),
    ]
