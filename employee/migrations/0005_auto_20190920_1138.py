# Generated by Django 2.1.7 on 2019-09-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_managermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='emp_Email',
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='emp_Address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_Firstname',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_Mobilenumber',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
