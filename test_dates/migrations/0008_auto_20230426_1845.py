# Generated by Django 3.2 on 2023-04-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_dates', '0007_auto_20230426_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='test',
        ),
        migrations.AddField(
            model_name='testresult',
            name='application',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='test_dates.testapplication'),
            preserve_default=False,
        ),
    ]
