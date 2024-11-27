# Generated by Django 5.0.8 on 2024-11-14 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0012_migrate_types_to_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventure',
            name='type',
        ),
        migrations.AlterField(
            model_name='adventure',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adventures.category'),
        ),
    ]