# Generated by Django 3.1.4 on 2021-01-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('fb_link', models.CharField(max_length=255)),
                ('insta_link', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
