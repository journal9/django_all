# Generated by Django 5.0.6 on 2024-05-14 14:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField()),
                ('reach', models.TextField(choices=[('in', 'In'), ('un', 'Un'), ('aus', 'Aus')], default='un')),
                ('rating', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.author')),
            ],
        ),
    ]