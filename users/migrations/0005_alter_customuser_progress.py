# Generated by Django 3.2 on 2023-04-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230426_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='progress',
            field=models.CharField(choices=[('1', 'Theory'), ('2', 'Obstacle'), ('3', 'Road'), ('4', 'Done')], max_length=1),
        ),
    ]
