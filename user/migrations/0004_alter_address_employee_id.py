# Generated by Django 4.0.1 on 2022-03-08 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='employee_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.employee'),
        ),
    ]
