# Generated by Django 3.1.6 on 2021-04-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtuber',
            name='cammera_type',
        ),
        migrations.AddField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('cannon', 'cannon'), ('red', 'red'), ('samsung', 'samsung'), ('others', 'others')], default='other', max_length=225),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('vlog', 'vlog'), ('cooking', 'cooking'), ('academic', 'academic'), ('adult', 'adult')], max_length=225),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large'), ('professional', 'professional')], max_length=225),
        ),
    ]
