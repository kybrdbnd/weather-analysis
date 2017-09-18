from django.db import models

# Create your models here.

class StationModel(models.Model):
	created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
	station_name = models.CharField(max_length=30)