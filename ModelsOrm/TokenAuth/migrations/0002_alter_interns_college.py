# Generated by Django 5.0.6 on 2024-06-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TokenAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interns',
            name='college',
            field=models.CharField(max_length=70),
        ),
    ]
