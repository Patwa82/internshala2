# Generated by Django 5.0.5 on 2025-01-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expenses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='users',
            field=models.ManyToManyField(to='users.customuser'),
        ),
    ]