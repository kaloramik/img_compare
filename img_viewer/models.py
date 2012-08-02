from django.db import models

# Create your models here.

class CompareInstance(models.Model):
    expected_img_url = models.CharField(max_length=200)
    new_img_url = models.CharField(max_length=200)
    diff_path = models.CharField(max_length=200)


