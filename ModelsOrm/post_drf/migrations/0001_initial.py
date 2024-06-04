# Generated by Django 5.0.6 on 2024-06-03 07:48

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.TextField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], default='male')),
                ('joined_date', models.DateField(default=datetime.date(2024, 6, 3))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('captain', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_drf.user', verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.CharField(max_length=50)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_drf.user')),
            ],
        ),
    ]