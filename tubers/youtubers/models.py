from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    camera_choices = [
        ('cannon', 'cannon'),
        ('red', 'red'),
        ('samsung', 'samsung'),
        ('others', 'others'),
    ]

    crew_choices = [
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
        ('professional', 'professional'),
    ]

    category_choices = [
        ('vlog', 'vlog'),
        ('cooking', 'cooking'),
        ('academic', 'academic'),
        ('adult', 'adult'),
    ]

    name = models.CharField(max_length = 225)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/ytubers/%Y/%m')
    video_url = models.CharField(max_length = 225)
    description = RichTextField()
    age = models.IntegerField()
    city = models.CharField(max_length = 225)
    age = models.IntegerField()
    crew = models.CharField(choices = crew_choices, max_length = 225)
    camera_type = models.CharField(choices = camera_choices, max_length = 225, default='other')
    subs_count = models.CharField(max_length = 225)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(choices = category_choices, max_length = 225)
    created_date = models.DateTimeField(default = datetime.now, blank=True)