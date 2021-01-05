from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    photo = models.ImageField(upload_to="media/slider/%Y")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline   