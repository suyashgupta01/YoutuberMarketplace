# Generated by Django 3.1.5 on 2021-01-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='role',
            field=models.CharField(default='something', max_length=255),
        ),
    ]
