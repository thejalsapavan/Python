# Generated by Django 4.2.7 on 2023-11-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aho', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='hostel',
            old_name='phn',
            new_name='PhoneNumber',
        ),
        migrations.RenameField(
            model_name='hostel',
            old_name='ad',
            new_name='nativePlace',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='np',
        ),
        migrations.AddField(
            model_name='hostel',
            name='Address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]