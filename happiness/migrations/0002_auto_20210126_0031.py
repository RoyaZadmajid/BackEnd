# Generated by Django 3.1.5 on 2021-01-26 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('happiness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
