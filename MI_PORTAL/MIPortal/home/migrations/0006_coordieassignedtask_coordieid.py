# Generated by Django 4.0.3 on 2022-03-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_coordieassignedtask_cg'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordieassignedtask',
            name='coordieID',
            field=models.CharField(default='k', max_length=10),
            preserve_default=False,
        ),
    ]
