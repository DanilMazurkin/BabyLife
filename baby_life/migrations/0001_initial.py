# Generated by Django 4.0 on 2021-12-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EatBabe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_when_eat', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SleepBaby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_when_sleep', models.DateTimeField(null=True)),
                ('datetime_when_not_sleep', models.DateTimeField(null=True)),
            ],
        ),
    ]
