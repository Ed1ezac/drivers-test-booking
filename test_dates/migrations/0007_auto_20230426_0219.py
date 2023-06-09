# Generated by Django 3.2 on 2023-04-26 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_dates', '0006_alter_testdate_test_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testapplication',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_dates.testdate'),
        ),
        migrations.AlterField(
            model_name='testdate',
            name='test_type',
            field=models.CharField(choices=[('1', 'Written'), ('2', 'Obstacle'), ('3', 'Road')], max_length=2),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_dates.testdate'),
        ),
    ]
