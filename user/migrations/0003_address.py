# Generated by Django 4.0.1 on 2022-03-08 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_employee_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
            ],
        ),
    ]
