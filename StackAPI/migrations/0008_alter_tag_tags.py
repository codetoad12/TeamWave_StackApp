# Generated by Django 3.2.5 on 2022-07-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StackAPI', '0007_alter_data_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tags',
            field=models.CharField(max_length=500),
        ),
    ]
