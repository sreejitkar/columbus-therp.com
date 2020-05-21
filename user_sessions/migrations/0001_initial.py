# Generated by Django 3.0.6 on 2020-05-21 04:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='session',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=None)),
                ('status', models.CharField(choices=[('1', 'ONGOING'), ('2', 'CLOSED'), ('3', 'TERMINATED')], default=1, max_length=100)),
                ('session_key', models.CharField(default=None, max_length=100)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
    ]