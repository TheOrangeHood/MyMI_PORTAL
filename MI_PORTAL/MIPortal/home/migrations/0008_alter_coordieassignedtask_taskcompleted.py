# Generated by Django 4.0.3 on 2022-03-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_coordieassignedtask_taskcompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordieassignedtask',
            name='taskCompleted',
            field=models.BooleanField(default='False'),
        ),
    ]
