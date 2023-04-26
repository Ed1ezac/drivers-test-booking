# Generated by Django 3.2 on 2023-04-25 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_dates', '0002_testdate_test_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_application', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='testdate',
            name='candidates',
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_result', models.CharField(choices=[('P', 'Pass'), ('F', 'Fail'), ('X', 'No Show')], max_length=1)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_dates.testapplication')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='test_dates.testdate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='testapplication',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='test_dates.testdate'),
        ),
        migrations.AddField(
            model_name='testapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
