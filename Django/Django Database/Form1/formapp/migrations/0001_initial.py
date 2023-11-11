# Generated by Django 4.2.7 on 2023-11-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=20)),
                ('empsalary', models.IntegerField()),
                ('empaddress', models.CharField(max_length=50)),
            ],
        ),
    ]
