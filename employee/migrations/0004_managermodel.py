# Generated by Django 2.1.7 on 2019-09-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190919_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=10)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('DOB', models.DateField(blank=True, default=None, max_length=100, null=True)),
                ('Company', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Manager information',
            },
        ),
    ]
