# Generated by Django 5.0.8 on 2024-09-22 04:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0006_alter_adventure_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventure',
            name='date',
        ),
        migrations.RemoveField(
            model_name='adventure',
            name='end_date',
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='adventures.adventure')),
            ],
        ),
    ]