# Generated by Django 2.1.4 on 2019-06-05 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_auto_20190603_1057'),
        ('task', '0003_task_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Gateway_task',
        ),
    ]
