# Generated by Django 3.1.5 on 2021-01-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.CharField(default='https://suyashgupta.me', max_length=255),
        ),
    ]
